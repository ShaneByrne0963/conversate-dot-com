from django.test import TestCase


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
