from forum.models import Tag
from django.db.models import Count
from django.utils.text import slugify
from django.shortcuts import get_object_or_404


# The maximum amount of tags that can be displayed in the side navigation
TAG_COLLAPSIBLE_LIMIT = 1


def get_top_tags(limit=TAG_COLLAPSIBLE_LIMIT):
    """
    Gets a set number of tags, sorted by the most number of posts with this
    tag, as well as a boolean for if there are more tags available
    """
    tags = list(Tag.objects.annotate(num_posts=Count('tagged_posts'))
                .order_by('-num_posts'))
    return {
        'top_tags': tags[:limit],
        'has_more_tags': (len(tags) > limit)
    }


def get_or_create_tag(tag_name):
    """
    Returns a tag with a specified name, or creates one if there is none
    """
    tag = list(Tag.objects.filter(name=tag_name))
    if len(tag) == 0:
        return Tag.objects.create(name=tag_name, slug=slugify(tag_name))
    else:
        return tag[0]


def update_tag(tag):
    """
    Removes a tag from the database if there are no posts attached to it
    """
    if tag.number_of_posts() == 0:
        tag.delete()
