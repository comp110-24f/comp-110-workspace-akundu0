"""Test file for find_max"""

__author__ = "730762344"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_rv() -> None:
    """find_and_remove_max should return the largest value of list."""
    a: list[int] = [9, 8, 4, 9, 7]
    assert find_and_remove_max(a) == 9


def test_find_and_remove_max_mutate() -> None:
    """All instances of the max value should be removes from input list."""
    a: list[int] = [9, 8, 4, 9, 7]
    find_and_remove_max(a)
    assert a == [8, 4, 7]


def test_find_and_remove_max_edge() -> None:
    """Should return -1 if list is empty."""
    a: list[int] = []
    assert find_and_remove_max(a) == -1
