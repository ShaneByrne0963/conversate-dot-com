from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Post, Tag, Comment, SiteData
from .core.content import get_profile, sort_posts
from .core.tags import get_top_tags
from .core.slug import generate_slug
from .core.pagination import get_paginated_posts
from .core.posting import convert_post_content
import urllib.parse


class ListPosts(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')

        posts = Post.objects.all()
        user_profile = get_profile(request.user)
        sort_by_new = user_profile.sort_by_new
        posts = sort_posts(posts, sort_by_new)
        top_tags = get_top_tags()

        context = get_paginated_posts(request, posts)
        if sort_by_new:
            context['heading'] = "What's New"
        else:
            context['heading'] = "What's Trending"
        context['selected_tab'] = 'Home'
        context['top_tags'] = top_tags

        return render(
            request,
            'index.html',
            context,
        )


class SortPosts(View):
    def get(self, request, by_new, current_dir):
        profile = get_profile(request.user)
        profile.sort_by_new = (by_new == 1)
        profile.save()
        return redirect(current_dir)


class SearchPost(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')

        # Redirects the user to the home page if no search query is given
        if 'search_query' not in request.GET:
            return redirect('home')
        search_input = request.GET.get('search_query')

        query = Q(Q(title__icontains=search_input) |
                  Q(content__icontains=search_input))
        posts = Post.objects.filter(query)
        user_profile = get_profile(request.user)
        sort_by_new = user_profile.sort_by_new
        posts = sort_posts(posts, sort_by_new)
        number_of_results = len(list(posts))

        # Constructing the heading
        heading = f'{number_of_results} Result'
        if number_of_results != 1:
            heading += 's'
        heading += f' for "{search_input}"'

        # Adding the extra details to the context
        context = get_paginated_posts(request, posts)
        context['heading'] = heading
        context['selected_tab'] = 'Search'
        context['search_result'] = search_input
        # Converting the form inputs into a url to insert into pagination
        search_formatted = urllib.parse.quote_plus(search_input)
        search_url = f'?search_query={search_formatted}'
        context['search_url'] = search_url

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
        tag = request.POST.get('tag')
        content = request.POST.get('content')
        content = convert_post_content(content)

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
