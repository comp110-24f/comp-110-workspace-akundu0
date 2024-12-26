"""File to define Bear class."""

__author__ = "730762344"


class Bear:
    """Initializes Bear object."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initializes bears to 0 age and 0 hunger."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Ages bears and decreases hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Bears eat fish based on hunger score."""
        self.hunger_score += num_fish
        return None
