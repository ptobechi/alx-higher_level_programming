#!/usr/bon/python3

"""
A rectanlge module that inherits basegeometry
"""


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        :return: A string containing information about the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

# r = Rectangle(3, 5)
#
# print(r)
# print(dir(r))
#
# try:
#   print("Rectangle: {} - {}".format(r.width, r.height))
# except Exception as e:
#   print("[{}] {}".format(e.__class__.__name__, e))
#
# try:
#   r2 = Rectangle(4, True)
# except Exception as e:
#  print("[{}] {}".format(e.__class__.__name__, e))
