#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the elements of the original list
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            # If the element doesn't match, add it to the new list as is
            new_list.append(element)

    return new_list
