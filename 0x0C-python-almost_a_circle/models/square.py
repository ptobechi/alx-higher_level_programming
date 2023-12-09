#!/usr/bin/python3

"""
a module that defines a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Notes:
        a square class that inherits a rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Note:
            class constructor that initialize instance of the Sqaure class
        Parameters:
            size - size of the square
            x - x axis
            y - y axis
            id - class id
        Raises:
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Notes:
            overide str representation of the square
        Returns:
            [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Note:
            public getter for the size of the sqaure
        Returns:
            the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Note:
            A public setter for the width and height of the square
        Properties:
            value - size of the width and height
        """
        self.width = value
        self.height = value

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
        attributes = ["id", "size", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Note:
            Return dictionary representation of the rectangle.

        Returns:
            Dictionary representation with keys: id, width, height, x, y.
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }
