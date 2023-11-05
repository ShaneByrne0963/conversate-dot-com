from django.contrib import admin
from .models import Post, Comment, Tag, SiteData
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('posted_on', 'tag')
    list_display = (
        'title',
        'tag',
        'posted_by',
        'posted_on',
        'number_of_likes'
    )
    search_fields = ('title', 'tag', 'posted_by')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_filter = ('posted_on',)
    list_display = (
        'content',
        'post',
        'posted_by',
        'posted_on',
        'number_of_likes'
    )


@admin.register(Tag)
class TagAdmin(SummernoteModelAdmin):

    list_display = ('name', 'number_of_posts')


@admin.register(SiteData)
class SiteDataAdmin(SummernoteModelAdmin):

    list_display = ('total_posts_created',)
