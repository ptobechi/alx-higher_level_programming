#!/usr/bin/python3

"""
a module that add all the elements of a python script
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_items_to_json():
    """
    Add all command line arguments to a Python list and save them to a JSON file.

    Usage:
    $ python add_items_to_json.py item1 item2 item3

    The items will be saved to a file named add_item.json.
    If the file doesn't exist, it will be created.
    No file permission exceptions are managed.
    """

    # Load existing items from the file, if any
    try:
        items_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items_list = []

    # Add command line arguments to the list
    items_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items_list, "add_item.json")
