def generate_slug(post_title, post_tag, total_posts):
    """
    Generates a slug for a post using it's title and tag, as well as the total
    number of posts as a seed to generate a set of random characters
    """
    # Error handling
    if not isinstance(post_title, str):
        raise TypeError("Title must be a string")
    if not isinstance(post_tag, str):
        raise TypeError("Tag must be a string")
    if not isinstance(total_posts, int):
        raise TypeError("The total number of posts must be an integer")
    return ''


def generate_character_set(seed, number_of_characters):
    """
    Generates a specified string of characters using a seed
    """
    # Error handling
    if not isinstance(seed, int):
        raise TypeError("Seed must be an integer")
    if not isinstance(number_of_characters, int):
        raise TypeError("Number of characters must be an integer")

    characters = ''
    for i in range(number_of_characters):
        characters += '0'

    return characters