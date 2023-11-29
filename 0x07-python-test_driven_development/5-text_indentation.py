#!/usr/bin/python3

"""
a python script that indents text after new characters
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char

        if char in separators:
            print(current_line.strip())
            print()  # Print two new lines
            current_line = ""

    if current_line.strip():
        print(current_line.strip())
