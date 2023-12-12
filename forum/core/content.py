from forum.models import Post, Profile
from .categories import get_top_categories
from .pagination import get_paginated_items, POSTS_PER_PAGE, \
                        CATEGORIES_PER_PAGE, POLLS_PER_PAGE
from django.contrib.auth.models import User
from django.db.models import Count


def get_base_context(request):
    """
    Builds the minimum context required for the base template to function
    correctly.
    """
    context = get_top_categories()
    context['disable_sort'] = True
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
