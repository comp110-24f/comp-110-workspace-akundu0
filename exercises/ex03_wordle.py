"""Wordle Exercise"""

__author__ = "730762344"


def input_guess(length: int) -> str:
    """Takes guess input from user"""
    guess: str = input(f"Enter a {length} character word: ")

    while len(guess) != length:  # makes sure guess is appropriate number of characters
        guess = input(f"That wasn't {length} chars! Try again: ")

    return guess


def contains_char(word: str, char: str) -> bool:
    """Searches word for character"""
    assert len(char) == 1  # ensures char is 1 character

    count: int = 0
    search: bool = False

    while (search == False) and (count < len(word)):
        if word[count] == char:  # checks if character is at specified index
            search = True
        count += 1
    return search


def emojified(guess_str: str, secret_word: str) -> str:
    """Compare 2 strings, return emoji comparison"""
    assert len(guess_str) == len(secret_word)  # checks that lengths are the same

    # emoji constants
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    results = ""
    count = 0

    while count < len(secret_word):
        if guess_str[count] == secret_word[count]:
            results = (
                results + GREEN_BOX
            )  # returns green box if character is in correct spot
        elif contains_char(secret_word, guess_str[count]):
            results = (
                results + YELLOW_BOX
            )  # returns yellow box if character is in the word but not in correct spot
        else:
            results = (
                results + WHITE_BOX
            )  # returns white box if character is not in word
        count += 1

    return results  # returns all boxes


def main(secret: str) -> None:
    """Entrypoint of the program"""
    turn: int = 0
    guess: str = ""

    while (
        turn < 6 and guess != secret
    ):  # stops when player reaches 6 turns or wins the game
        turn += 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(5)  # prompts user for guess
        print(emojified(guess, secret))  # prints emoji corresponding to guess

    if guess == secret:  # player wins
        print(f"You won in {turn}/6 turns!")
    else:  # player lost
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
