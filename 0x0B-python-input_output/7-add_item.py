#!/usr/bin/python3

"""
a module that add all the elements of a python script
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_json():
    """
    Add all command line arguments to a Python list and
    save them to a JSON file.

    Usage:
    $ python add_items_to_json.py item1 item2 item3

    The items will be saved to a file named add_item.json.
    If the file doesn't exist, it will be created.
    No file permission exceptions are managed.
    """
    file_name = "add_item.json"

    # Load existing list from the file if it exists
    if os.path.exists(file_name):
        my_list = load_from_json_file(file_name)
    else:
        my_list = []

    # Add new items from command line arguments
    my_list.extend(args)

    # Save the updated list to the JSON file
    save_to_json_file(my_list, file_name)

    # Print the updated list
    print(my_list)


if __name__ == "__main__":
    # Remove script name from arguments
    arguments = sys.argv[1:]

    # Add items to the list and save to JSON file
    add_items_to_json(arguments)
