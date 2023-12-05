#!/usr/bin/python3

"""
a module that add all the elements of a python script
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys
import os
import json


def add_items_to_json(args):
    """
    Add all command line arguments to a Python list and
    save them to a JSON file using fopen and fwrite.

    Parameters:
    - args (list): List of command line arguments.

    Usage:
    $ python add_items_to_json.py item1 item2 item3

    The items will be saved to a file named add_item.json.
    If the file doesn't exist, it will be created.
    No file permission exceptions are managed.
    """
    file_name = "add_item.json"

    # Load existing list from the file if it exists
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            my_list = json.load(file)
    else:
        my_list = []

    # Add new items from command line arguments
    my_list.extend(args)

    # Save the updated list to the JSON file
    with open(file_name, 'w') as file:
        json.dump(my_list, file)

    # Print the updated list
    print(my_list)

if __name__ == "__main__":
    # Remove script name from arguments
    arguments = sys.argv[1:]

    # Add items to the list and save to JSON file
    add_items_to_json(arguments)
