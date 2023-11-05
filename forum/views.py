from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import Post, Tag, SiteData
from .core.slug import generate_slug


class PostList(View):
    paginate_by = 20

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('accounts/login')

        posts = Post.objects.order_by('-posted_on')
        p = Paginator(posts, self.paginate_by)
        page = request.GET.get('page')
        current_posts = p.get_page(page)

        context = {
            'post_list': current_posts,
            'paginator': p
        }
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
