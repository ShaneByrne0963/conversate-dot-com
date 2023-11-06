from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('new-post', views.AddPost.as_view(), name='new_post'),
    path('<slug:slug>/', views.ViewPost.as_view(), name='view_post')
]
