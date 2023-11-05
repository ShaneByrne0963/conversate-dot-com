import unittest
from slug import generate_slug, generate_character_set, get_character


class TestSlug(unittest.TestCase):
    """
    Test cases for slug.generate_slug function
    """
    def test_throws_error_if_title_is_not_string(self):
        self.assertRaises(TypeError, generate_slug, 0, 'Tag', 1)

    def test_throws_error_if_tag_is_not_string(self):
        self.assertRaises(TypeError, generate_slug, 'Hello World', ['Tag'], 1)

    def test_throws_error_if_total_posts_is_not_integer(self):
        self.assertRaises(TypeError, generate_slug, 'Hello World', 'Tag', '42')

    def test_generate_slug_returns_string(self):
        self.assertIsInstance(generate_slug('Hello World', 'Tag', 42), str)

    def test_slugified_tag_in_returned_string(self):
        self.assertTrue(
            'test-tag' in generate_slug('Hello World', 'Test Tag', 42)
        )

    def test_character_set_in_returned_string(self):
        self.assertTrue('SoMUq2gZ' in generate_slug('Hello World', 'Tag', 0))

    def test_slugified_title_in_returned_string(self):
        self.assertTrue('hello-world' in generate_slug('Hello World', 'Tag', 0))


class TestRandomCharacterSet(unittest.TestCase):
    """
    Test cases for slug.generate_character_set function
    """
    def test_throws_error_if_seed_is_not_integer(self):
        self.assertRaises(TypeError, generate_character_set, '64', 15)

    def test_throws_error_if_char_number_is_not_integer(self):
        self.assertRaises(TypeError, generate_character_set, 64, '15')

    def test_generate_character_set_returns_string(self):
        self.assertIsInstance(generate_character_set(1000, 10), str)

    def test_length_of_output_matches_number_of_characters(self):
        self.assertEqual(len(generate_character_set(0, 10)), 10)

    def test_seed_0_returns_consistent_character_set(self):
        self.assertEqual(generate_character_set(0, 8), 'SoMUq2gZ')

    def test_seed_100_returns_consistent_character_set(self):
        self.assertEqual(generate_character_set(100, 8), '9ttYNbJp')


class TestGetCharacter(unittest.TestCase):
    """
    Test cases for slug.get_character function
    """
    def test_throws_error_if_index_is_not_integer(self):
        self.assertRaises(TypeError, get_character, 'index')

    def test_throws_error_if_index_is_less_than_0(self):
        self.assertRaises(IndexError, get_character, -1)

    def test_throws_error_if_index_is_greater_than_61(self):
        self.assertRaises(IndexError, get_character, 62)

    def test_get_character_returns_string(self):
        self.assertIsInstance(get_character(0), str)

    def test_index_less_than_10_returns_digit(self):
        self.assertEqual(get_character(6), '6')

    def test_index_between_10_and_35_returns_lowercase_letter(self):
        self.assertEqual(get_character(35), 'z')

    def test_index_between_36_and_61_returns_uppercase_letter(self):
        self.assertEqual(get_character(61), 'Z')


unittest.main()
