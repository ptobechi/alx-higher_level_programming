#!/usr/bin/python3

"""
A module that shows is an object inherit directly or indirectly
from a specified class
"""


def inherits_from(obj, a_class):
    """
    inherits_from:
        True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    :param obj:
        The object to check.
    :param a_class:
        The class to compare against.
    :Return:
        True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

# a = True
# if inherits_from(a, int):
#   print("{} inherited from class {}".format(a, int.__name__))
# if inherits_from(a, bool):
#   print("{} inherited from class {}".format(a, bool.__name__))
# if inherits_from(a, object):
#  print("{} inherited from class {}".format(a, object.__name__))
