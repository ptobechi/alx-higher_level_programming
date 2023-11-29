#!/usr/bin/python3

"""
A python script that sum up two integer
"""



def add_integer(a, b=98):
    """
    add_integer:
        sum upn to integers
    Parameters:
        a (int): first integer
        b (int): second integer
    Raises:
        TypeError: if any of the parameters is not an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # cast the integers if they are floats value
    a = int(a)
    b = int(b)

    #return result of the addition
    return a + b

