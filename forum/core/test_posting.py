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

    def test_returns_input_wrapped_in_paragraph_tags(self):
        self.assertEqual(convert_post_content('Hello'), '<p>Hello</p>')

    def test_returns_multiple_paragraphs_with_new_lines(self):
        self.assertEqual(
            convert_post_content('Hello\nWorld!'),
            '<p>Hello</p><p>World!</p>'
        )

    def test_replaces_empty_paragraphs_with_line_breaks(self):
        self.assertEqual(
            convert_post_content('Hello\n\nWorld!'),
            '<p>Hello</p><br><p>World!</p>'
        )

    def test_trims_paragraphs_of_white_space(self):
        self.assertEqual(
            convert_post_content('Hello\n \nWorld!'),
            '<p>Hello</p><br><p>World!</p>'
        )


unittest.main()
