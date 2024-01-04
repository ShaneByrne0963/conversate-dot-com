from forum.models import Category
from django.db.models import Count


# The maximum amount of tags that can be displayed in the side navigation
CATEGORY_COLLAPSIBLE_LIMIT = 6


def get_top_categories(limit=CATEGORY_COLLAPSIBLE_LIMIT):
    """
    Gets a set number of categories, sorted by the most number of posts with
    this category, as well as a boolean for if there are more categories
    available
    """
    categories = list(Category.objects
                      .annotate(num_posts=Count('tagged_posts'))
                      .filter(num_posts__gt=0)
                      .order_by('-num_posts'))
    num_categories = len(categories)

    # Preventing "No Category" from showing up on the list
    category_none = Category.objects.get(slug='none')
    if category_none in categories:
        categories.remove(category_none)

    return {
        'num_categories': num_categories,
        'top_categories': categories[:limit],
        'has_more_categories': (len(categories) > limit)
    }
