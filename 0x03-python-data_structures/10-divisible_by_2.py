#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []  # Create an empty list to store True/False values

    for num in my_list:
        result.append(num % 2 == 0)  # Append True if the number is divisible by 2, otherwise append False

    return result
