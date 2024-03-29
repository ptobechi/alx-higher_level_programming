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

    def __str__(self):
        """Returns the string representation of the rectangle"""
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result

        for element in range(self.__height):
            for ele in range(self.__width):
                result += "#"
            if element < self.__height - 1:
                result += '\n'

        return result

    def __repr__(self):
        """Returns the official string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

# my_rectangle = Rectangle(2, 4)
# print(str(my_rectangle))
# print("--")
# print(my_rectangle)
# print("--")
# print(repr(my_rectangle))
# print("--")
# print(hex(id(my_rectangle)))
# print("--")
#
# create new instance based on representation
# new_rectangle = eval(repr(my_rectangle))
# print(str(new_rectangle))
# print("--")
# print(new_rectangle)
# print("--")
# print(repr(new_rectangle))
# print("--")
# print(hex(id(new_rectangle)))
# print("--")
#
# print(new_rectangle is my_rectangle)
# print(type(new_rectangle) is type(my_rectangle))
