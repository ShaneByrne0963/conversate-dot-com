from django.core.paginator import Paginator
from forum.tests import test_instance, test_index


# The maximum amount of pages that can be displayed in the pagination bar
# Must be an odd number to have the current page in the middle
NUM_PAGES = 9
POSTS_PER_PAGE = 20
CATEGORIES_PER_PAGE = 48
POLLS_PER_PAGE = 10


def get_paginated_items(request, object_list, items_per_page):
    """
    Paginates a list of items from a model
    """
    p = Paginator(object_list, items_per_page)
    page = request.GET.get('page')
    current_items = p.get_page(page)

    pagination_context = {
        'item_list': current_items,
        'page': page
    }

    if page is None:
        page = 1
    if p.num_pages > NUM_PAGES:
        pagination_context.update(get_page_range(
            int(page),
            p.num_pages
        ))
    else:
        pagination_context['page_range'] = p.page_range

    return pagination_context


def get_page_range(page_index, last_page, num_pages=NUM_PAGES):
    """
    Creates a range of page numbers, with the value of page_index in the
    middle. There must be as many pages as (or more than) the number of
    visible pages (i.e. last_page >= num_pages)
    """
    # Error handling
    test_instance(page_index, int, 'page_index must be an integer')
    test_instance(last_page, int, 'last_page must be an integer')
    test_instance(num_pages, int, 'num_pages must be an integer')
    test_index(page_index, 1, last_page)
    if num_pages < 1:
        raise IndexError('num_pages must be at least 1')
    if last_page < num_pages:
        raise IndexError('More pages than the number of visible pages')
    if num_pages % 2 == 0:
        raise ValueError('num_pages cannot be even')

    # Calculating how many pages will sit in between the current page
    # The 3 represents the first page, the current page and the last page,
    pages_one_side = (num_pages - 3) // 2

    lower_limit = page_index - pages_one_side
    upper_limit = page_index + pages_one_side
    # Will be used to display "..." between page gaps
    start_gap = True
    end_gap = True

    # The page range cannot include the first or last page. They will be
    # added later
    if lower_limit <= 2:
        upper_limit += 2 - lower_limit
        lower_limit = 2
        start_gap = False
    elif upper_limit >= last_page - 1:
        lower_limit += last_page - 1 - upper_limit
        upper_limit = last_page - 1
        end_gap = False

    page_range = list(range(lower_limit, upper_limit + 1))
    # Adding the first and last page
    page_range.insert(0, 1)
    page_range.append(last_page)

    page_info = {
        'page_range': page_range,
        'start_gap': start_gap,
        'end_gap': end_gap
    }
    return page_info
