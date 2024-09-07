"""Challenge Question 00: Functions"""

__author__ = "730762344"


def mimic(message: str) -> str:
    """Repeat input"""
    return message


def main() -> None:
    """Print message"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
