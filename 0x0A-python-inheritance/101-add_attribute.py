#!/usr/bin/python3

"""
a module adding a new attribute to an object
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    :param obj: The object to which the attribute will be added.
    :param attribute: The name of the attribute.
    :param value: The value of the attribute.
    :raises TypeError: If the object can't have a new attribute.
    """
    if hasattr(obj, "__dict__") or (hasattr(obj, "__slots__")
                                    and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

# class MyClass():
#   pass
#
# mc = MyClass()
# add_attribute(mc, "name", "John")
# print(mc.name)
#
# try:
#   a = "My String"
#   add_attribute(a, "name", "Bob")
#   print(a.name)
# except Exception as e:
#  print("[{}] {}".format(e.__class__.__name__, e))
