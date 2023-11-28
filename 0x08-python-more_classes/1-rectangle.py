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

# my_rectangle = Rectangle(2, 4)
# print(my_rectangle.__dict__)
#
# my_rectangle.width = 10
# my_rectangle.height = 3
# print(my_rectangle.__dict__)