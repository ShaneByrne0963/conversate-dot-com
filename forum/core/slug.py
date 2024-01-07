import random
import re
from django.utils.text import slugify
from forum.tests import test_instance, test_index
from forum.models import SiteData


SLUG_CHARACTERS = 8


def generate_slug(post_title, category_slug):
    """
    Generates a slug for a post using it's title and category, as well as the
    total number of posts as a seed to generate a set of random characters
    """
    # Error handling
    test_instance(post_title, str, 'title must be a string')
    test_instance(category_slug, str, 'tag must be a string')

    # Finding the total number of posts
    site_data = list(SiteData.objects.all())
    site_data_object = None
    if len(site_data) == 0:
        site_data_object = SiteData.objects.create()
    else:
        site_data_object = site_data[0]
    total_posts = site_data_object.total_posts_created

    # Getting all the components of the slug
    character_set = generate_character_set(total_posts, SLUG_CHARACTERS)
    slugified_title = slugify(post_title)

    # Adding another post to the total posts created
    total_posts += 1
    site_data_object.total_posts_created = total_posts
    site_data_object.save()

    return f'{category_slug}-{character_set}-{slugified_title}'


def generate_character_set(seed, number_of_characters):
    """
    Generates a specified string of characters using a seed
    """
    # Error handling
    test_instance(seed, int, 'seed must be an integer')
    test_instance(number_of_characters, int,
                  'num_of_characters must be an integer')
    test_index(number_of_characters, 1, 100)

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

    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    # Digits
    if index < 10:
        return str(index)
    if index <= 35:
        return letters[index - 10]
    return letters[index - 36].upper()


def format_tag_search(tag_list):
    """
    Removes all special characters, with the exception of "-" and "_",
    from a string, and replaces spaces with "+"
    """
    # Error Handling
    test_instance(tag_list, str, "tag_list must be a string")

    formatted_tags = ''.join(re.findall(r'\s|[a-zA-Z0-9_-]', tag_list))
    formatted_tags = formatted_tags.replace(' ', '+')
    return formatted_tags
