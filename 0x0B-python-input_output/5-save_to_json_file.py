#!/usr/bin/python3

"""
a function that writes an object to python file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Parameters:
    - my_obj: The object to be serialized and written to the file.
    - filename (str): The name of the file.

    Note:
    - This function uses the with statement for proper file handling.
    - No exceptions are managed if the object can't be serialized.
    - No file permission exceptions are managed.

    Example:
        >>> my_dict = {"name": "John", "age": 25}
        >>> save_to_json_file(my_dict, "output.json")
    """

    with open(filename, "w") as file:
        json_string = json.dumps(my_obj)
        file.write(json_string)
