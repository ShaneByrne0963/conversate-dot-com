import unittest
from posting import convert_post_content


class TestPosting(unittest.TestCase):
    """
    Test cases for posting.convert_post_content function
    """

    def test_throws_error_if_content_input_is_not_string(self):
        self.assertRaises(TypeError, convert_post_content, {
                'content': 'Hello World'
            }
        )

    def test_convert_post_content_returns_string(self):
        self.assertIsInstance(convert_post_content('Hello'), str)


unittest.main()
