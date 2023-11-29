#!/usr/bin/python3

"""
a python script that prints a square
"""


def print_square(size):
    """
    Prints a square with the character #.

    Parameters:
        size (int): Size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
