def test_instance(variable, var_type, error_message):
    """
    Tests if a variable is of a certain instance, and raises a TypeError
    if it isn't
    """
    if not isinstance(variable, var_type):
        raise TypeError(error_message)


def generate_slug(post_title, post_tag, total_posts):
    """
    Generates a slug for a post using it's title and tag, as well as the total
    number of posts as a seed to generate a set of random characters
    """
    # Error handling
    test_instance(post_title, str, 'title must be a string')
    test_instance(post_tag, str, 'tag must be a string')
    test_instance(total_posts, int, 'total_posts must be an integer')
    return ''


def generate_character_set(seed, number_of_characters):
    """
    Generates a specified string of characters using a seed
    """
    # Error handling
    test_instance(seed, int, 'seed must be an integer')
    test_instance(number_of_characters, int,
                  'num_of_characters must be an integer')

    characters = ''
    for i in range(number_of_characters):
        characters += '0'

    return characters


generate_slug('Title', 'Tag', 42)
