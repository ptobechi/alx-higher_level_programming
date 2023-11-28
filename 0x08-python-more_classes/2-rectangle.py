#!/usr/bin/python3

"""
A python script that defines a Rectangle class.

The class represents a rectangle shape and serve as a prototype
to creating and manipulating a rectangle object

Attributes:
    __width (int): set the width of the rectangle. Default = 0
    __height (int): set the height of the rectangle. Default = 0
Methods:
    __init__(self, width=0, height=0): initialize new instance of the class
"""


class Rectangle:
    """
    A Rectangle class

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
    Methods:
        __init__(self, witdth=0, height=0): set the initial value of the
        width and height to 0
    """
    def __init__(self, width=0, height=0):
        """
        initilizes a new instance of the class

        Parameters:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter property for the width of the rectangle

        Returns:
            The width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Getter property for the height of the rectangle

        Returns:
            The height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter property for the width of the rectangle

        Parameters:
            value (int): the expected width of the rectangle
        Raises:
            TypeError: if the provided value is not an integer
            ValueError: if the provided value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter property for the height of the rectangle

        Parameters;
            value (int): sets the expected value for the height of
            the rectangle
        Raises:
            TypeError: if the provided value is not an integer
            ValueError: if the provided value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        area:
            calculates the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter:
            calculates the perimeter of the rectangles
        Returns:
            if width or height is equal to 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__height + self.__width)

# my_rectangle = Rectangle(2, 4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
# my_rectangle.perimeter()))
#
# print("--")
#
# my_rectangle.width = 10
# my_rectangle.height = 3
# print("Area: {}- Perimeter: {}".format(my_rectangle.area(),
# my_rectangle.perimeter()))
