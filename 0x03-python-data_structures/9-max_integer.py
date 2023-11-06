#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    max_num = my_list[0]  # Initialize max_num with the first element

    for num in my_list:
        if num > max_num:
            max_num = num

    return max_num
