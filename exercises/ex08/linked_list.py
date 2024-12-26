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


def value_at(head: Node | None, index: int) -> int:
    """Returns value at specific index of Node."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        index -= 1
        if (head.next is None) and index > 0:
            raise IndexError("Index is out of bounds on the list.")
        head = head.next
        return value_at(head, index)


def max(head: Node | None) -> int:
    """Returns maximum value in Node object."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    find_max = max(head.next)
    if head.value > find_max:
        return head.value
    return find_max


def linkify(items: list[int]) -> Node | None:
    """Returns Node object from input list."""
    if len(items) > 0:
        rest: Node = Node(items[0], linkify(items[1:]))
        return rest
    else:
        return None


def scale(head: Node | None, factor: int) -> Node | None:
    """Scales up Node with certain factor."""
    if head is None:
        return None
    else:
        new: Node = Node(head.value * factor, scale(head.next, factor))
        return new
