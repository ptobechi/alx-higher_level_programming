#!/usr/bin/python3

"""
a module based of on 6-geometry module
"""


class BaseGeometry:
    """
    A class representing the base geometry.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value.

        :param name: A string representing the name of the value.
        :param value: The value to be validated.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

# bg = BaseGeometry()
# bg.integer_validator("my_int", 12)
# bg.integer_validator("width", 89)
#
# try:
#   bg.integer_validator("name", "John")
# except Exception as e:
#   print("[{}] {}".format(e.__class__.__name__, e))
#
# try:
#   bg.integer_validator("age", 0)
# except Exception as e:
#  print("[{}] {}".format(e.__class__.__name__, e))
#
# try:
#   bg.integer_validator("distance", -4)
# except Exception as e:
#  print("[{}] {}".format(e.__class__.__name__, e))
