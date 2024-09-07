"""Tea party planner"""

__author__: str = "730762344"


# Outputs calculations
def main_planner(guests: int) -> None:
    """Prints output of planner"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Computes the number of tea bags needed"""
    return 2 * people  # Assumes 2 teas per person


def treats(people: int) -> int:
    """Computes number of treats needed"""
    return int(1.5 * tea_bags(people=people))  # assumes 1.5 treats per tea


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate total cost of treats and tea bags combined."""

    return (0.5 * tea_count) + (
        0.75 * treat_count
    )  # adds cost of tea and cost of treats


# Runs program, takes input
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
