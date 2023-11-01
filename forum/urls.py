from . import views
from django.urls import path


urlpatterns = [
    path('home', views.PostList.as_view(), name='home'),
    path('new-post', views.AddPost.as_view(), name='new_post'),
    path('', views.SignIn.as_view(), name='login'),
]
