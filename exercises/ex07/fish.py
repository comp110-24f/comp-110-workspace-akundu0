"""File to define Fish class."""

__author__ = "730762344"


class Fish:
    """initializes fish object."""

    age: int

    def __init__(self) -> None:
        """Initializes fish to 0 age."""
        self.age = 0
        return None

    def one_day(self) -> None:
        """Ages fish per day."""
        self.age += 1
        return None
