#!/usr/bin/python3

"""
a module that returns the dictionary description with simple python data
structure
"""


def class_to_json(obj):
    """
    Return a dictionary description with a simple data structure
    for JSON serialization of an object.

    Parameters:
    - obj: An instance of a Class.

    Returns:
    - dict: The dictionary description with a simple data structure.

    Note:
    - All attributes of the obj Class must be serializable: list,
      dictionary, string, integer, and boolean.

    Example:
        >>> class MyClass:
        ...     def __init__(self, name, age, hobbies):
        ...         self.name = name
        ...         self.age = age
        ...         self.hobbies = hobbies
        ...
        >>> obj_instance = MyClass(name="John", age=25,
        ...                        hobbies=["Reading", "Gaming"])
        >>> json_dict = class_to_json(obj_instance)
        >>> print(json_dict)
        {'name': 'John', 'age': 25, 'hobbies': ['Reading', 'Gaming']}
    """

    json_dict = {}
    for attr_name in dir(obj):
        if not callable(getattr(obj, attr_name)) and \
           not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value

    return json_dict
