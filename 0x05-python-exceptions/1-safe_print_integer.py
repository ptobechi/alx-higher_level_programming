#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print()
        return True
    except ValueError:
        print("{} is not an integer".format(value))
        return False

safe_print_integer("Hello")

