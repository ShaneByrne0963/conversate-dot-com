from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('new-post', views.AddPost.as_view(), name='new_post'),
    path('<slug:slug>/', views.ViewPost.as_view(), name='view_post'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like_post')
]
