"""File to define River class."""

__author__ = "730762344"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Initializes River object."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks if bears and fish die of old age."""
        copy: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                copy.append(fish)
        self.fish = copy
        copy2: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                copy2.append(bear)
        self.bears = copy2
        return None

    def check_hunger(self) -> None:
        """Checks if bears starve."""
        copy: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                copy.append(bear)
        self.bears = copy
        return None

    def repopulate_fish(self) -> None:
        """Simulates fish reproduction."""
        n = len(self.fish)
        for i in range(4 * (n // 2)):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Simulates bear reproduction."""
        n = len(self.bears)
        for i in range(n // 2):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """Prints contents of river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes fish from river."""
        while amount != 0:
            self.fish.pop(0)
            amount -= 1
        return None

    def bears_eating(self) -> None:
        """Each bear eats 3 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulates one week in the river."""
        for i in range(7):
            self.one_river_day()
        return None
