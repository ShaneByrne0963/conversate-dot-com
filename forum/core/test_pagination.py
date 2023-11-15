import unittest
from pagination import get_page_range, NUM_PAGES


class TestPagination(unittest.TestCase):
    """
    Test cases for pagination.get_page_range function
    """
    def test_throws_error_if_page_index_is_not_number(self):
        self.assertRaises(TypeError, get_page_range, 'One', 10)

    def test_throws_error_if_last_page_is_not_number(self):
        self.assertRaises(TypeError, get_page_range, 4, '10')

    def test_throws_error_if_num_pages_is_not_number(self):
        self.assertRaises(TypeError, get_page_range, 4, 10, '')

    def test_throws_error_if_page_index_is_less_than_1(self):
        self.assertRaises(IndexError, get_page_range, 0, 10)

    def test_throws_error_if_page_index_is_greater_than_last_page(self):
        self.assertRaises(IndexError, get_page_range, 12, 11)

    def test_throws_error_if_last_page_is_less_than_num_pages(self):
        self.assertRaises(IndexError, get_page_range, 1, 4, 5)

    def test_throws_error_if_num_pages_is_less_than_1(self):
        self.assertRaises(IndexError, get_page_range, 4, 10, 0)

    def test_throws_error_if_num_pages_is_not_even(self):
        self.assertRaises(ValueError, get_page_range, 4, 10, 6)

    def test_get_page_range_returns_range_of_length_num_pages_minus_2(self):
        self.assertEqual(len(get_page_range(5, 10, 5)), 3)

    def test_page_range_middle_index_is_page_index_for_non_clamped_range(self):
        self.assertEqual(get_page_range(11, 32, 5)[1], 11)

    def test_page_range_never_contains_the_first_page(self):
        self.assertEqual(get_page_range(2, 32, 9)[0], 2)

    def test_page_range_never_contains_the_last_page(self):
        self.assertEqual(get_page_range(29, 32, 9)[6], 31)


unittest.main()
