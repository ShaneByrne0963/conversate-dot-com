from . import views
from django.urls import path


urlpatterns = [
    path('', views.PopularPosts.as_view(), name='home'),
    path('new', views.RecentPosts.as_view(), name='recent_posts'),
    path('<slug:slug>/', views.ViewPost.as_view(), name='view_post'),
    path('search', views.SearchPost.as_view(), name='search_post'),
    path('new-post', views.AddPost.as_view(), name='new_post'),
    path('edit/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like_post'),
    path('delete/<slug:slug>', views.DeletePost.as_view(), name='delete_post'),
    path(
        'comment/<slug:slug>',
        views.SendComment.as_view(),
        name='send_comment'
    ),
    path(
        'like-comment/<int:comment_id>',
        views.LikeComment.as_view(),
        name='like_comment'
    ),
    path(
        'edit-comment/<int:comment_id>',
        views.EditComment.as_view(),
        name='edit_comment'
    ),
    path(
        'delete-comment/<int:comment_id>',
        views.DeleteComment.as_view(),
        name='delete_comment'
    )
]
