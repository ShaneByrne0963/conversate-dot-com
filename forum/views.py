from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Post, Tag
from .forms import PostForm


class SignIn(View):

    def get(self, request):
        return render(
            request,
            'sign_in.html',
            {},
        )


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-posted_on')
    template_name = 'index.html'
    paginate_by = 15


class AddPost(View):

    def get(self, request):
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

        Post.objects.create(
            title=title,
            content=content,
            tag=tag_object,
            posted_by=request.user
        )

        return redirect('home')
