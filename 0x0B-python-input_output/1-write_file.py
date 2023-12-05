#!/usr/bin/python3

"""
A module that write a string to text (utf-8)
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return
    the number of characters written.

    Parameters:
        filename (str, optional): The name of the file.
        Defaults to an empty string.
        text (str, optional): The string to be written to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.

    Note:
        This function uses the with statement for proper file handling.
        No file permission exceptions are managed.
        The function creates the file if it doesn't exist and
        overwrites its content if it already exists.
        No modules are imported.

    Example:
        >>> write_file("example.txt", "This is a sample text.")
    """

    with open(filename, "w", encoding="utf-8") as file:
        char_count = file.write(text)
    return char_count
