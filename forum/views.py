from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Count, Q
from .models import Post, Tag, Comment, SiteData
from .core.slug import generate_slug
from .core.pagination import get_page_range


POSTS_PER_PAGE = 3


def get_paginated_posts(request, post_list):
    """
    Paginates a list of posts
    """
    p = Paginator(post_list, POSTS_PER_PAGE)
    page = request.GET.get('page')
    current_posts = p.get_page(page)

    return {
        'post_list': current_posts,
        'paginator': p
    }


class PopularPosts(View):
    paginate_by = 20

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')

        posts = Post.objects \
                    .annotate(num_likes=Count('likes')) \
                    .order_by('-num_likes')
        context = get_paginated_posts(request, posts)
        context['heading'] = "What's Trending"
        context['selected_tab'] = 'Popular'

        return render(
            request,
            'index.html',
            context,
        )


class RecentPosts(View):
    paginate_by = 20

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        posts = Post.objects.order_by('-posted_on')
        context = get_paginated_posts(request, posts)
        context['heading'] = "What's New"
        context['selected_tab'] = 'Recent'

        return render(
            request,
            'index.html',
            context,
        )


class SearchPost(View):
    paginate_by = 20

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')

        # Redirects the user to the home page if no search query is given
        if 'search_query' not in request.GET:
            return redirect('home')

        search_input = request.GET.get('search_query')
        filter_by = request.GET.get('filter_by')
        query = Q(Q(title__icontains=search_input) |
                  Q(content__icontains=search_input))
        posts = None
        if filter_by == 'popular':
            posts = Post.objects \
                .filter(query) \
                .annotate(num_likes=Count('likes')) \
                .order_by('-num_likes')
        else:
            posts = Post.objects.filter(query).order_by('-posted_on')
        number_of_results = len(list(posts))

        heading = f'{number_of_results} Result'
        if number_of_results != 1:
            heading += 's'
        heading += f' for "{search_input}"'

        context = get_paginated_posts(request, posts)
        context['heading'] = heading
        context['selected_tab'] = 'Search'
        context['search_result'] = search_input
        context['search_filter'] = filter_by
        # Converting the form inputs into a url to insert into pagination
        search_url = f'?search_query={search_input}&filter_by={filter_by}'
        context['search_url'] = search_url.replace(' ', '+')

        return render(
            request,
            'index.html',
            context,
        )


class AddPost(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        context = {}
        return render(
            request,
            'new_post.html',
            context,
        )

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        tag = request.POST.get('tag')

        # Add the tag to the database if the tag doesn't already exist
        existing_tag = list(Tag.objects.filter(name=tag))
        tag_object = None
        if len(existing_tag) == 0:
            tag_object = Tag.objects.create(name=tag)
        else:
            tag_object = existing_tag[0]

        # Generating the slug for the post
        site_data = get_object_or_404(SiteData)
        total_posts = site_data.total_posts_created
        post_slug = generate_slug(title, tag, total_posts)
        total_posts += 1
        site_data.total_posts_created = total_posts
        site_data.save()

        Post.objects.create(
            title=title,
            slug=post_slug,
            content=content,
            tag=tag_object,
            posted_by=request.user
        )
        return redirect('home')


class EditPost(View):

    def get(self, request, slug):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        post = get_object_or_404(Post, slug=slug)
        context = {
            'post': post
        }
        return render(
            request,
            'edit_post.html',
            context,
        )

    def post(self, request, slug):
        title = request.POST.get('title')
        content = request.POST.get('content')
        tag = request.POST.get('tag')
        post = get_object_or_404(Post, slug=slug)

        post.title = title
        post.content = content
        post.edited = True
        post.approved = False

        if post.tag.name != tag:
            print('Different Tags')
            # Add the tag to the database if the tag doesn't already exist
            existing_tag = list(Tag.objects.filter(name=tag))
            tag_object = None
            if len(existing_tag) == 0:
                tag_object = Tag.objects.create(name=tag)
            else:
                tag_object = existing_tag[0]
            post.tag = tag_object

        post.save()
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class ViewPost(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('-posted_on')
        liked = post.likes.filter(id=request.user.id).exists()
        context = {
            'post': post,
            'comments': comments,
            'liked': liked
        }
        return render(
            request,
            'post_details.html',
            context
        )


class LikePost(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class DeletePost(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('home')


class SendComment(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_text = request.POST.get('content')
        reply_id = request.POST.get('reply')
        reply_to = None

        if reply_id is not None:
            reply_to = get_object_or_404(Comment, id=int(reply_id))

        Comment.objects.create(
            post=post,
            content=comment_text,
            posted_by=request.user,
            reply_to=reply_to
        )
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class LikeComment(View):

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)

        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)

        # Finding the slug of the post the comment is on
        post = comment.post
        slug = post.slug
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class EditComment(View):

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        updated_body = request.POST.get('content')

        comment.content = updated_body
        comment.edited = True
        comment.save()

        # Finding the slug of the post the comment is on
        post = comment.post
        slug = post.slug
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class DeleteComment(View):

    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        post = comment.post
        slug = post.slug
        comment.delete()
        return HttpResponseRedirect(reverse('view_post', args=[slug]))
