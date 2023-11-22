from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Post, Tag, Comment, SiteData
from .core.content import get_profile, get_post_list_context, get_base_context
from .core.tags import get_or_create_tag, update_tag
from .core.slug import generate_slug
from .core.posting import convert_post_content
import urllib.parse


class ListPosts(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')

        posts = Post.objects.all()

        context = get_post_list_context(request, posts)
        user_profile = get_profile(request.user)
        if user_profile.sort_by_new:
            context['heading'] = "What's New"
        else:
            context['heading'] = "What's Trending"
        context['selected_tab'] = 'Home'

        return render(
            request,
            'post_list.html',
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
        number_of_results = len(list(posts))

        # Constructing the heading
        heading = f'{number_of_results} Result'
        if number_of_results != 1:
            heading += 's'
        heading += f' for "{search_input}"'

        # Adding the extra details to the context
        context = get_post_list_context(request, posts)
        context['heading'] = heading
        context['selected_tab'] = 'Search'
        context['search_result'] = search_input
        # Converting the form inputs into a url to insert into pagination
        search_formatted = urllib.parse.quote_plus(search_input)
        search_url = f'?search_query={search_formatted}'
        context['search_url'] = search_url

        return render(
            request,
            'post_list.html',
            context,
        )


class TaggedPosts(View):
    def get(self, request, tag_slug):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')

        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tag=tag)

        context = get_post_list_context(request, posts)
        context['heading'] = f'Posts tagged with "{tag.name}"'
        context['selected_tab'] = f'Tags/{tag.name}'

        return render(
            request,
            'post_list.html',
            context,
        )


class MyPosts(View):
    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')

        posts = Post.objects.filter(posted_by=request.user)

        context = get_post_list_context(request, posts)
        context['heading'] = f'Your Posts'
        context['selected_tab'] = 'My Posts'

        return render(
            request,
            'post_list.html',
            context,
        )


class AddPost(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        context = get_base_context(request)
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
        tag_object = get_or_create_tag(tag)

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

        previous_tag = post.tag
        if previous_tag.name != tag:
            post.tag = get_or_create_tag(tag)
            update_tag(previous_tag)

        post.save()
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class ViewPost(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('-posted_on')
        liked = post.likes.filter(id=request.user.id).exists()
        context = get_base_context(request)
        context.update({
            'post': post,
            'comments': comments,
            'liked': liked
        })
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
        tag = post.tag
        post.delete()
        update_tag(tag)
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
