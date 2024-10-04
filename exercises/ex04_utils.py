"""List utils"""

__author__ = "730762344"


def all(a_list: list[int], num: int) -> bool:
    is_same: bool = False
    i: int = 0
    while i < len(a_list):
        if a_list[i] == num:
            is_same = True
        else:
            is_same = False
        i += 1
    return is_same


def max(a_list: list[int]) -> int:
    if len(a_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest: int = 0

    while i < len(a_list):
        if a_list[i] > largest:
            largest = a_list[i]


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):
        return False
    else:
        i: int = 0
        while i < len(list_1):
            if list_1[i] == list_2[i]:
                i += 1
            else:
                return False
        return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    i: int = 0

    while i < len(list_2):
        list_1.append(list_2[i])
        i += 1
    return None
