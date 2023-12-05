#!/usr/bin/python3

"""
A module that read text from a file
"""


def read_file(filename=""):
    """
    Read a text file (UTF-8) and print its content to stdout.

    Parameters:
        filename (str, optional): The name of the file.
        Defaults to an empty string.

    Note:
        This function uses the with statement for proper file handling.
        No file permission or non-existent file exceptions are managed.
        No modules are imported.

    Example:
        >>> read_file("example.txt")
        This is the content of the text file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end='')
