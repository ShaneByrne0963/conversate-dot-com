import unittest
from posting import convert_post_content


class TestPosting(unittest.TestCase):
    """
    Test cases for pagination.get_page_range function
    """

    def test_throws_error_if_content_input_is_not_string(self):
        self.assertRaises(TypeError, convert_post_content, {
                'content': 'Hello World'
            }
        )


unittest.main()
