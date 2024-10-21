"""Unit tests for utils.py!"""

__author__ = "730762344"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_rv() -> None:
    """Tests that only_evens returns list with only evens"""
    a: list[int] = [4, 9, 2, 6, 7]
    assert only_evens(a) == [4, 2, 6]


def test_only_evens_mutate() -> None:
    """Tests only_evens if the original input list is mutated."""
    a: list[int] = [4, 9, 2, 6, 7]
    only_evens(a)
    assert a == [4, 9, 2, 6, 7]


def test_only_evens_edge() -> None:
    a: list[int] = [6, 6, 6]
    only_evens(a)
    assert a == [6, 6, 6]


def test_sub_edge() -> None:
    """Tests sub if the empty input list returns an empty list."""
    a: list[int] = []
    assert sub(a, 3, -2) == []


def test_sub_rv() -> None:
    """Tests the return value of sub function"""
    a: list[int] = [2, 3, 1, 4, 5]
    assert sub(a, 1, 3) == [3, 1]


def test_sub_mutate() -> None:
    """Tests that sub function does not mutate original function"""
    a: list[int] = [1, 2, 3, 4]
    sub(a, 2, 4)
    assert a == [1, 2, 3, 4]


def test_add_at_index_edge() -> None:
    """Tests that add_at_index raises an error for invalid index."""
    a: list[int] = [1, 2, 3, 4]
    with pytest.raises(IndexError):
        add_at_index(a, 3, 7)


def test_add_at_index_rv() -> None:
    """Tests that add_at_index returns nothing"""
    a: list[int] = [1, 2, 3, 4]
    assert add_at_index(a, 2, 2) == None


def test_add_at_index_mutate() -> None:
    """Tests that add_at_index mutates original list"""
    a: list[int] = [1, 2, 3, 4]
    add_at_index(a, 2, 2)
    assert a == [1, 2, 2, 3, 4]
