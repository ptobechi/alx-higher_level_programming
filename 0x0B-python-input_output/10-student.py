#!/usr/bin/python3

"""
a module that defines a student by firstname, lastname and age
"""


class Student:
    """
    Class representing a student.

    Attributes:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Parameters:
        - attrs (list, optional): A list of attribute names to be retrieved.
          Defaults to None.

        Returns:
        - dict: A dictionary representation with a simple data structure
          for JSON serialization.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            json_dict = {attr: getattr(self, attr) for attr
                         in attrs if hasattr(self, attr)}
        else:
            json_dict = {}
            for attr_name in dir(self):
                if not callable(getattr(self, attr_name)) and \
                                not attr_name.startswith("__"):
                    attr_value = getattr(self, attr_name)
                    if isinstance(attr_value, (str, int)):
                        json_dict[attr_name] = attr_value
        return json_dict
