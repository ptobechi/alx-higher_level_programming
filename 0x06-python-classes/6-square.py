#!/usr/bin/python3

"""
This script defines a Square class.

The Square class represents a square shape and
provides a simple way to create and manipulate square objects.

Attributes:
    __size (int): The size of each side of the square. Default is 0.

Methods:
    __init__(self, size=0): Initializes a new instance of the Square class.
"""


class Square:

    """
    A class to represent a square.

    Attributes:
        __size (int): The size of each side of the square. Default is 0.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of each side of the square. Default is 0.
            size (int): The size must be greater than 0
        Errors:
            TypeError: raise a type error if size not an integer
            ValueError: raise an error if size is less than error
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2 or not all(
                isinstance(element, int) and element >= 0 for element in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter property for the size of the square
        Return:
            The value/size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter property for the size of the square.

        Parameters:
            value (int): The new size of each side of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter property for the position of the square
        Return:
            The position of the square
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """
        Setter property for the size of the square.

        Parameters:
            value (tupple): the position of the square.

        Raises:
            TypeError: If the provided position is not a tuple of 2 int.
        """

        if not isinstance(value, tuple) or len(value) == 2 or all(
                element >= 0 and isinstance(element, int) for element in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        
    def area(self):
        """
        area: 
            calculate the area the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a visual representation of the square.
        length: 
            position of the square

        height:
            position of the square

        If the size is 0, prints an empty line. Otherwise,
        prints '#' repeated 'size' times on each line.
        """

        length = self.__position[0]
        height = self.__position[1]

        if self.__size == 0:
            print()
            return

        for i in range(height):
            print()

        for i in range(self.__size):
            if length > 0:
                print(" "*length, end="")
            print("#" * self.__size)


# my_square_1 = Square(3)
# my_square_1.my_print()

# print("--")

# my_square_2 = Square(3, (1, 3))
# my_square_2.my_print()

# print("--")

# my_square_3 = Square(3, (3, 0))
# my_square_3.my_print()

# print("--")
