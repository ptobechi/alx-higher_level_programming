#!/usr/bin/python3

"""
a module that appends a line to the text of a file
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific
    string in a file.

    Parameters:
    - filename (str): The name of the file.
    - search_string (str): The string to search for in each line.
    - new_string (str): The line of text to insert after each line
      containing the search string.

    Note:
    - This function uses the with statement for proper file handling.
    - No file permission or non-existent file exceptions are managed.
    - No modules are imported.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")
