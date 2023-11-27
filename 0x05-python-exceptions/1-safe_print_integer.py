#!/usr/bin/python3

def safe_print_integer(value):
    isInt = False
    try:
        print("{:d}".format(value))
        isInt = True
    except ValueError:
        isInt = False
    finally:
        return isInt
