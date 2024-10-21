"""Return max num from list"""

__author__ = "730762344"


def find_and_remove_max(input: list[int]) -> int:
    """Returns max int in input and removes all instances of it"""
    if len(input) == 0:
        return -1  # returns -1 if list is empty

    # searches list for max with for loop
    largest: int = input[0]
    for item in input:
        if item > largest:
            largest = item

    # removes all instances of max value
    i: int = 0
    while i < len(input):
        if input[i] == largest:
            input.pop(i)
        else:
            i += 1
    return largest
