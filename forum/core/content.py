from forum.models import Post, Profile, Category, Poll, PollAnswer
from .categories import get_top_categories
from .pagination import get_paginated_items, POSTS_PER_PAGE, \
                        CATEGORIES_PER_PAGE, POLLS_PER_PAGE
from django.contrib.auth.models import User
from forum.forms import PostContentForm
from django.db.models import Count
from datetime import datetime
import cloudinary
import re


def get_base_context(request):
    """
    Builds the minimum context required for the base template to function
    correctly.
    """
    context = get_top_categories()
    context['disable_sort'] = True
    return context


def get_post_context(request, post):
    context = get_base_context(request)
    context['post'] = post
    context['comments'] = post.comments.order_by('-posted_on')
    return context


def get_post_list_context(request, post_list):
    """
    Builds the minimum context required for the post_list template to function
    """
    context = get_base_context(request)

    user_profile = get_profile(request.user)
    sort_by_new = user_profile.sort_by_new
    posts_sorted = sort_posts(post_list, sort_by_new)

    context.update(get_paginated_items(request, posts_sorted, POSTS_PER_PAGE))
    context['disable_sort'] = False
    return context


def get_category_list_context(request, category_list):
    """
    Builds the minimum context required for the category_list
    template to function
    """
    context = get_base_context(request)
    context['item_list'] = category_list
    context.update(get_paginated_items(request, category_list,
                                       CATEGORIES_PER_PAGE))
    return context


def get_poll_list_context(request, poll_list):
    """
    Builds the minimum context required for the poll_list template to function
    """
    context = get_base_context(request)
    context['item_list'] = poll_list
    context.update(get_paginated_items(request, poll_list, POLLS_PER_PAGE))
    return context


def get_post_form_context(request):
    """
    Builds the minimum context required for the add/edit post templates
    to function
    """
    context = get_base_context(request)
    categories = Category.objects.all()
    context['category_list'] = categories
    context['content_form'] = PostContentForm()
    return context


def create_poll(request, post=None):
    """
    Creates a Poll object and adds it to the database
    """
    title = request.POST.get('poll-title')
    due_date = request.POST.get('due-date')
    # Date format: YYYY-MM-DD
    due_year = int(due_date[:4])
    due_month = int(due_date[5:7])
    due_day = int(due_date[8:])

    poll = Poll.objects.create(
        title=title,
        asked_by=request.user,
        post=post,
        due_date=datetime(due_year, due_month, due_day)
    )

    # Creating each answer specified by the user
    for input_name in request.POST:
        if 'answer-' in input_name:
            position = int(''.join(re.findall(r'[0-9]', input_name)))
            PollAnswer.objects.create(
                body=request.POST[input_name],
                poll=poll,
                position=position
            )


def get_profile(user_object):
    """
    Gets a user's profile, or creates one if none exists
    """
    profile = list(Profile.objects.filter(user=user_object))
    if len(profile) > 0:
        return profile[0]
    else:
        new_profile = Profile.objects.create(
            user=user_object,
            sort_by_new=False
        )
        return new_profile


def sort_posts(post_list, by_new):
    """
    Sorts a list of posts by highest number of likes or by most recent
    """
    if by_new:
        return post_list.order_by('-posted_on')
    else:
        return post_list.annotate(num_likes=Count('likes')) \
                        .order_by('-num_likes')


def delete_image(post):
    """
    Deletes an image from a post
    """
    if post.image:
        cloudinary.uploader.destroy(post.image.public_id)
