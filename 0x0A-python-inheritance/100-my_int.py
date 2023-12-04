#!/usr/bin/python3

"""
a module class inheriting an int class
"""


class MyInt(int):
    """
    A class representing an integer with inverted equality operators.
    """

    def __eq__(self, other):
        """
        Inverts the equality operator (==).

        :param other: The value to compare with.
        :return: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator (!=).

        :param other: The value to compare with.
        :return: True if equal, False if not equal.
        """
        return super().__eq__(other)

# my_i = MyInt(3)
# print(my_i)
# print(my_i == 3)
# print(my_i != 3)
