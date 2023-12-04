#!/usr/bin/python3

"""
A module based on 5-geometry module
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

# bg = BaseGeometry()
# try:
#   print(bg.area())
# except Exception as e:
#  print("[{}] {}".format(e.__class__.__name__, e))
