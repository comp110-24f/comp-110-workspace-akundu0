"""Practicing while loops over a string"""

__author__ = "730762344"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = (
        0  # will keep track of the number of times the search_char is in the phrase
    )

    i: int = 0

    while i <= len(phrase) - 1:
        if search_char == phrase[i]:  # adds to count if char is in phrase
            count += 1

        i += 1  # brings loop closer to condition

    return count
