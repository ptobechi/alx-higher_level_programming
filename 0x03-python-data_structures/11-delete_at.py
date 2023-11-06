#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # If idx is negative or out of range, return the same list

    new_list = []  # Create a new list to store the updated items

    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])  # Append items except the one at the specified position

    return new_list
