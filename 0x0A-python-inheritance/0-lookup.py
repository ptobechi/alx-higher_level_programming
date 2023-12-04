#!/usr/bin/python3

"""
This module contains functions and classes related to Class Inheritance
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: A list containing the attributes and methods of the object.
    """
    return [attr for attr in dir(obj)]

# class MyClass1(object):
#  pass

# class MyClass2(object):
#  my_attr1 = 3
#   def my_meth(self):
#       pass
# print(lookup(MyClass1))
# print(lookup(MyClass2))
# print(lookup(int))
