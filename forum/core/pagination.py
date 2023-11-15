# The maximum amount of pages that can be displayed in the pagination bar
# Must be an odd number to have the current page in the middle
NUM_PAGES = 5
POSTS_PER_PAGE = 2


def test_instance(variable, var_type, error_message):
    """
    Tests if a variable is of a certain instance, and raises a TypeError
    if it isn't
    """
    if not isinstance(variable, var_type):
        raise TypeError(error_message)


def test_index(number, min_range, max_range):
    """
    Tests if a number is within a certain range, and raises an IndexError
    if it isn't
    """
    if number < min_range:
        raise IndexError(f'index should not be less than {min_range}')
    elif number > max_range:
        raise IndexError(f'index should not be greater than {max_range}')


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
    # added later
    if lower_limit <= 1:
        upper_limit += 2 - lower_limit
        lower_limit = 2
    elif upper_limit >= last_page:
        lower_limit += last_page - 1 - upper_limit
        upper_limit = last_page - 1

    page_range = list(range(lower_limit, upper_limit + 1))
    # Adding the first and last page
    page_range.insert(0, 1)
    page_range.append(last_page)
    return page_range
