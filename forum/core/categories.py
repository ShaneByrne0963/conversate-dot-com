from forum.models import Category
from django.db.models import Count


# The maximum amount of tags that can be displayed in the side navigation
CATEGORY_COLLAPSIBLE_LIMIT = 1


def get_top_categories(limit=CATEGORY_COLLAPSIBLE_LIMIT):
    """
    Gets a set number of categories, sorted by the most number of posts with
    this category, as well as a boolean for if there are more tags available
    """
    tags = list(Category.objects.annotate(num_posts=Count('tagged_posts'))
                .order_by('-num_posts'))
    return {
        'top_categories': tags[:limit],
        'has_more_categories': (len(tags) > limit)
    }
