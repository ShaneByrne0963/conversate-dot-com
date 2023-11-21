from forum.models import Post, Profile
from django.contrib.auth.models import User
from django.db.models import Count


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
