"""More utility functions!"""

__author__ = "730762344"


def only_evens(input: list[int]) -> list[int]:
    """Returns list with even numbers"""
    evens: list[int] = []
    for item in input:
        if (item % 2) == 0:
            evens.append(item)
    return evens


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Returns subset of inputted list from starting to ending index"""
    subset: list[int] = []
    if start < 0:
        start = 0
    if end > len(input):
        end = len(input)
    if len(input) == 0 or start >= len(input) or end <= 0:
        return []

    while start != end:
        subset.append(input[start])
        start += 1

    return subset


def add_at_index(input: list[int], add: int, index: int) -> None:
    """Places element at given index in list"""
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")

    if index == len(input):
        input.append(add)
    else:
        input.append(0)
        i: int = len(input) - 1
        while i != index:
            input[i] = input[i - 1]
            i -= 1
        input[index] = add
