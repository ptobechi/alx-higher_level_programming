#!/usr/bin/python3

"""
A module that checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class; otherwise False.

    :param obj:
        The object to check.
    :param a_class:
        The class to compare against.
    :Return:
        True if obj is an instance of a_class or its subclasses,
        False otherwise.
    """
    return isinstance(obj, a_class)

# a = 1
# if is_kind_of_class(a, int):
#  print("{} comes from {}".format(a, int.__name__))
# if is_kind_of_class(a, float):
#  print("{} comes from {}".format(a, float.__name__))
# if is_kind_of_class(a, object):
#  print("{} comes from {}".format(a, object.__name__))
