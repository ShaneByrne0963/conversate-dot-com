from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('new-post', views.NewPost.as_view(), name='new_post'),
]
