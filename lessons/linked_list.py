"""Recursion EX08!"""

from __future__ import annotations


class Node:
    """Object for linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializes variables to object."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        # called automatically when converting an object to a string
        rest: str = "TODO"
        # TODO: Figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(courses)


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: When head is the last node
    print(f"Enter last({head.value})")
    if head.next is None:
        return head.value
    else:
        # Recursive case:
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest


print(last(one))  # expect to print 2
print(last(courses))  # expect to print 301


def recursive_range(start: int, end: int) -> Node | None:
    """build a list recursively from start to end."""
    if start > end:
        # Edge case
        raise ValueError("Invalid arguments, start > end")
    if start == end:
        # Base case
        return None
    else:
        # Recursive case
        # 1. Handle the first value in your new list here:
        first: int = start
        # 2. Let the rest of the list be handled recursively:
        rest: Node | None = recursive_range(start + 1, end)
        # 3. Return a new node which is first followed by rest
        return Node(first, rest)


a_list: Node | None = recursive_range(110, 113)
