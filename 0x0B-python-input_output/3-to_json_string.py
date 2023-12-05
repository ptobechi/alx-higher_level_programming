#!/usr/bin/python3

"""
A module that represents the json representation of an object
"""


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Parameters:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.

    Note:
        No exceptions are managed if the object can't be serialized.

    Example:
        >>> my_dict = {"name": "John", "age": 25}
        >>> json_string = to_json_string(my_dict)
        >>> print(json_string)
        '{"name": "John", "age": 25}'
    """

    json_string = str(my_obj)
    return json_string
