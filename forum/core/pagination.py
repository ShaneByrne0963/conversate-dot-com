from slug import test_instance, test_index


# The maximum amount of pages that can be displayed in the pagination bar
# Must be an odd number to have the current page in the middle
NUM_PAGES = 5


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

    # The page range cannot include the first or last page. They will be
    # handled separately
    if lower_limit <= 1:
        upper_limit += 2 - lower_limit
        lower_limit = 2
    elif upper_limit >= last_page:
        lower_limit += last_page - 1 - upper_limit
        upper_limit = last_page - 1

    page_range = range(lower_limit, upper_limit + 1)
    return page_range
