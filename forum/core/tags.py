from forum.models import Tag
from django.db.models import Count


# The maximum amount of tags that can be displayed in the side navigation
TAG_COLLAPSIBLE_LIMIT = 10


def get_top_tags(limit=TAG_COLLAPSIBLE_LIMIT):
    tags = list(Tag.objects.annotate(num_posts=Count('tagged_posts'))
                .order_by('-num_posts'))
    return tags[:limit]
