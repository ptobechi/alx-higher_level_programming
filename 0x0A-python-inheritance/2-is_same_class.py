#!/usr/bin/python3
"""
a module that check if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    is_same_class:
        True if the object is exactly an instance of the specified class
        otherwise False.

    :param obj:
        The object to check.
    :param a_class:
        The class to compare against.
    :Return:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class

# a = 1
# if is_same_class(a, int):
#   print("{} is an instance of the class {}".format(a, int.__name__))
# if is_same_class(a, float):
#  print("{} is an instance of the class {}".format(a, float.__name__))
# if is_same_class(a, object):
#  print("{} is an instance of the class {}".format(a, object.__name__))
