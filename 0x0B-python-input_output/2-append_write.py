#!/usr/bin/python3

"""
a module that appends to a file
"""

def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8) and
    return the number of characters added.

    Parameters:
        filename (str, optional): The name of the file.
        Defaults to an empty string.
        text (str, optional): The string to be appended to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.

    Note:
        This function uses the with statement for proper file handling.
        If the file doesn't exist, it will be created.
        No file permission or non-existent file exceptions are managed.
        No modules are imported.

    Example:
        >>> append_write("example.txt", " This is additional text.")
    """

    with open(filename, "a", encoding="utf-8") as file:
        char_added = file.write(text)
    return char_added
