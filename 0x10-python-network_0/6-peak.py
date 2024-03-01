#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: Peak value found in the list.
    """
    if not list_of_integers:
        return None

    start, end = 0, len(list_of_integers) - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]

