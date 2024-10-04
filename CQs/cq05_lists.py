"""Mutating functions."""

__author__ = "730762344"


def manual_append(a_list: list[int], num: int) -> None:
    """Appends int to inputted list"""
    a_list.append(num)


def double(a_list: list[int]) -> None:
    """Doubles each element in list"""
    i: int = 0
    while i < len(a_list):
        a_list[i] = a_list[i] * 2  # loops through list and doubles each element
        i += 1  # increment

    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
