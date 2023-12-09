#!/usr/bin/python3

"""
a rectangle module that inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
    Note:
        a rectangle class
    Attributes:
        __width, __height,.x,.y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Note:
            constructor class, initializing new instance of the class
        Parameters:
            width, height, x, y and id
        Raises:
            TypeError: if height or width is not an integer
            ValueError: if width or height is less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Note:
            the public getter for the width
        Return:
            the size/width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Note:
            the public setter for the width
        Parameters:
            value = width of the rectangle
        Raises:
            TypeError (int)
            ValueError (<= 0)
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value <= 0:
            raise ValueError("value must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Note:
            public getter for the height
        Returns:
            the size or height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Note:
            the public setter for the height of the rectangle
        Parameters:
            value - the size of the rectangle height
        Raises:
            TypeError (int)
            ValueError (<= 0)
        """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__height = value

    def area(self):
        """
        Note:
            calculate the area of the triangle
        Return:
            rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """
        Note:
            print class intances with #
        """
        for i in range(self.y):
            print()

        for element in range(self.__height):
            if self.x > 0:
                print(" " * self.x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Notes:
            overide str representation of the rectangle
        Returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        new_str = (
                f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.__width}/{self.__height}"
                )
        return new_str

    def update(self, *args, **kwargs):
        """
        Notes:
            assign argument to each attribute
        Parameters:
            args (no-keyword arguments): The order is important.
            1st argument: id attribute
            2nd argument: width attribute
            3rd argument: height attribute
            4th argument: x attribute
            5th argument: y attribute
            kwargs (dict): Key-value pairs where keys
            represent attributes to be updated.
        """
        num_args = len(args)
        if args:
            self.id = args[0]
        if num_args > 1:
            self.__width = args[1]
        if num_args > 2:
            self.__height = args[2]
        if num_args > 3:
            self.x = args[3]
        if num_args > 4:
            self.y = args[4]

        if 'id' in kwargs:
            self.__id = kwargs['id']
        if 'width' in kwargs:
            self.__width = kwargs['width']
        if 'height' in kwargs:
            self.__height = kwargs['height']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """
        Note:
            dictionary representation of the rectangle class
        Return:
            the dictionary rep of the class with vlaues
            (id, width, height,x ,y)
        """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width,
        }
