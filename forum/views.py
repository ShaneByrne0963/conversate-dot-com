from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-posted_on')
    template_name = 'index.html'
    paginate_by = 15


class NewPost(View):

    def get(self, request):
        return render(
            request,
            'new_post.html',
            {},
        )
