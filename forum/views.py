from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.db.models import Q, Count
from .models import Post, Category, Comment, SiteData
from .core.content import get_profile, get_post_list_context, \
                          get_base_context, get_category_list_context
from .core.pagination import get_paginated_items
from .core.slug import generate_slug, format_tag_search
from .core.posting import convert_post_content
import urllib.parse
import cloudinary


class ListPosts(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

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
            return redirect('/accounts/login')

        # Redirects the user to the home page if no search query is given
        if 'search_query' not in request.GET:
            return redirect('home')
        search_input = request.GET.get('search_query')

        # Searching by tags if a hashtag is at the beginning of the search
        if search_input.strip()[0] == '#':
            search_formatted = format_tag_search(search_input)
            print(search_formatted)
            return HttpResponseRedirect(reverse('search_tag',
                                                args=[search_formatted]))

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


class SearchTag(View):

    def get(self, request, tag_query):
        tag_list = tag_query.split('+')
        search_result = ''

        if tag_list:
            query = Q(tags__icontains=tag_list[0])
            for tag in range(1, len(tag_list)):
                query = query | Q(tags__icontains=tag_list[tag])
            posts = Post.objects.filter(query)
            number_of_results = len(list(posts))

            # Constructing the heading
            heading = f'{number_of_results} Post'
            if number_of_results != 1:
                heading += 's'
            heading += ' tagged with '
            for i in range(len(tag_list)):
                heading += f'"{tag_list[i]}"'
                search_result += f'#{tag_list[i]}'
                if i < len(tag_list) - 1:
                    heading += ', '
                    search_result += ' '

            # Adding the extra details to the context
            context = get_post_list_context(request, posts)
            context['heading'] = heading
            context['selected_tab'] = 'Tags'
            context['search_result'] = search_result

            return render(
                request,
                'post_list.html',
                context,
            )


class CategorisedPosts(View):
    def get(self, request, category_slug):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category)

        context = get_post_list_context(request, posts)
        context['heading'] = f'Posts in "{category.name}"'
        context['selected_tab'] = f'Category/{category.name}'

        return render(
            request,
            'post_list.html',
            context,
        )


class BrowseCategories(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        categories = Category.objects \
                             .annotate(num_posts=Count('tagged_posts')) \
                             .order_by('-num_posts')

        context = get_category_list_context(request, categories)
        context['selected_tab'] = 'Browse Categories'

        return render(
            request,
            'category_list.html',
            context,
        )


class MyPosts(View):
    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

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
            return redirect('/accounts/login')
        context = get_base_context(request)
        categories = Category.objects.all()
        context['category_list'] = categories
        return render(
            request,
            'new_post.html',
            context,
        )

    def post(self, request):
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')
        content = convert_post_content(content)
        tags = request.POST.get('tags')
        category_object = Category.objects.get(name=category)

        image_url = None
        image_position = None
        if request.FILES:
            image = request.FILES['post-image']
            image_url = cloudinary.uploader.upload(image)['public_id']
        image_position = request.POST.get('image-position')

        # Generating the slug for the post
        site_data = get_object_or_404(SiteData)
        total_posts = site_data.total_posts_created
        post_slug = generate_slug(title, category, total_posts)
        total_posts += 1
        site_data.total_posts_created = total_posts
        site_data.save()

        Post.objects.create(
            title=title,
            slug=post_slug,
            content=content,
            image=image_url,
            image_position=image_position,
            category=category_object,
            tags=tags,
            posted_by=request.user
        )
        return redirect('home')


class EditPost(View):

    def get(self, request, id):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        post = get_object_or_404(Post, id=id)

        # Preventing users that do not own the post from being able to edit it
        if post.posted_by != request.user:
            return HttpResponseRedirect(reverse('view_post', args=[post.slug]))

        context = get_base_context(request)
        context['post'] = post
        categories = Category.objects.all()
        context['category_list'] = categories
        return render(
            request,
            'edit_post.html',
            context,
        )

    def post(self, request, id):
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        tags = request.POST.get('tags')
        post = get_object_or_404(Post, id=id)

        post.title = title
        post.content = content
        post.edited = True
        post.approved = False
        post.category = Category.objects.get(name=category)
        post.tags = tags

        # Updating the image if a new one has been selected
        if request.FILES:
            image = request.FILES['post-image']
            image_url = cloudinary.uploader.upload(image)['public_id']
            # Removing any previous image from cloudinary
            if post.image:
                cloudinary.uploader.destroy(post.image.public_id)
            post.image = image_url
        post.image_position = request.POST.get('image-position')

        post.save()
        return HttpResponseRedirect(reverse('view_post', args=[post.slug]))


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
        if post.image:
            cloudinary.uploader.destroy(post.image.public_id)
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
