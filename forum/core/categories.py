from forum.models import Category
from django.db.models import Count


# The maximum amount of tags that can be displayed in the side navigation
CATEGORY_COLLAPSIBLE_LIMIT = 10


def get_top_categories(limit=CATEGORY_COLLAPSIBLE_LIMIT):
    """
    Gets a set number of categories, sorted by the most number of posts with
    this category, as well as a boolean for if there are more categories
    available
    """
    categories = list(Category.objects.annotate(num_posts=Count('tagged_posts'))
                      .order_by('-num_posts'))

    # Preventing "No Category" from showing up on the list
    category_none = Category.objects.get(slug='none')
    categories.remove(category_none)

    return {
        'top_categories': categories[:limit],
        'has_more_categories': (len(categories) > limit)
    }
