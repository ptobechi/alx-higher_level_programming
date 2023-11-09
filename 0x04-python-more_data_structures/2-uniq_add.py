#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()  # Create a set to store unique integers
    total = 0

    for num in my_list:
        if num not in unique_set:
            total += num
            unique_set.add(num)

    return total
