#!/usr/bin/python3

"""
A rectangle module that inherits basegeometry
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

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        :return: A string containing information about the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

# Rectangle = __import__('9-rectangle').Rectangle
#
# r = Rectangle(3, 5)
#
# print(r)
# print(r.area())
