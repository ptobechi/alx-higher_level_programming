#!/usr/bin/python3

"""
a module that creates an object from a file
"""

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file.

    Returns:
    - object: The Python data structure represented by the JSON file.

    Note:
    - This function uses the with statement for proper file handling.
    - No exceptions are managed if the JSON string doesn't represent an object.
    - No file permission exceptions are managed.

    Example:
        >>> loaded_obj = load_from_json_file("input.json")
        >>> print(loaded_obj)
        {'name': 'John', 'age': 25}
    """

    with open(filename, "r") as file:
        json_string = file.read()
        python_obj = eval(json_string)
    return python_obj
