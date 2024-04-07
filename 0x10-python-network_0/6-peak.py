#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    a function that finds a peak in a list of unsorted integers

    Args:
    list_of_integers (list of int): List of unsorted integers.

    Returns:
    int or None: The peak element, or None if the list is empty.

    """
    if not list_of_integers:
        return None

    start, end = 0, len(list_of_integers) - 1
    while start < end:
        mid = (start + end) // 2
        if list_of_integers[mid] > list_of_integers[mid - 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]
