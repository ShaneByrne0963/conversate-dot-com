import random
from django.utils.text import slugify
from forum.tests import test_instance, test_index


def generate_slug(post_title, post_tag, total_posts):
    """
    Generates a slug for a post using it's title and tag, as well as the total
    number of posts as a seed to generate a set of random characters
    """
    # Error handling
    test_instance(post_title, str, 'title must be a string')
    test_instance(post_tag, str, 'tag must be a string')
    test_instance(total_posts, int, 'total_posts must be an integer')

    # Getting all the components of the slug
    slugified_tag = slugify(post_tag)
    character_set = generate_character_set(total_posts, 8)
    slugified_title = slugify(post_title)

    return f'{slugified_tag}-{character_set}-{slugified_title}'


def generate_character_set(seed, number_of_characters):
    """
    Generates a specified string of characters using a seed
    """
    # Error handling
    test_instance(seed, int, 'seed must be an integer')
    test_instance(number_of_characters, int,
                  'num_of_characters must be an integer')

    characters = ''
    random.seed(seed)
    for i in range(number_of_characters):
        index = random.randint(0, 61)
        new_character = get_character(index)
        characters += new_character

    return characters


def get_character(index):
    """
    Gets a character with a specified index
    - 0-9 returns their respective number
    - 10-35 returns a lowercase letter
    - 36-61 returns an uppercase letter
    """
    test_instance(index, int, 'index must be an integer')
    test_index(index, 0, 61)

    letters = (
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
    )

    # Digits
    if index < 10:
        return str(index)
    if index <= 35:
        return letters[index - 10]
    return letters[index - 36].upper()
