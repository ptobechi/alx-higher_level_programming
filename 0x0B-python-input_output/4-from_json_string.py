#!/usr/bin/python3

"""
a module that returns an object of python data structure
"""
import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    Parameters:
    - my_str (str): The JSON string to be converted to a Python object.

    Returns:
    - object: The Python data structure represented by the JSON string.

    Note:
    - No exceptions are managed if the JSON string doesn't represent an object.

    Example:
        >>> json_string = '{"name": "John", "age": 25}'
        >>> my_dict = from_json_string(json_string)
        >>> print(my_dict)
        {'name': 'John', 'age': 25}
    """

    python_obj = json.dumps(my_str)
    return python_obj
