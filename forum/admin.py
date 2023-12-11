from django.contrib import admin
from .models import Profile, Post, Comment, Category, SiteData, Poll, \
                    PollAnswer
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('user', 'sort_by_new')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('posted_on', 'category')
    list_display = (
        'title',
        'category',
        'posted_by',
        'posted_on',
        'number_of_likes'
    )
    search_fields = ('title', 'category', 'posted_by')
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


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'number_of_posts')


@admin.register(Poll)
class PollAdmin(SummernoteModelAdmin):

    list_display = ('title', 'asked_by', 'number_of_answers', 'due_date')


@admin.register(PollAnswer)
class PollAnswerAdmin(SummernoteModelAdmin):

    list_display = ('body', 'poll', 'number_of_votes')


@admin.register(SiteData)
class SiteDataAdmin(SummernoteModelAdmin):

    list_display = ('total_posts_created',)
