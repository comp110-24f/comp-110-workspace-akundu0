"""Practice with conditionals"""

__author__ = "730762344"


def guess_a_number() -> None:
    secret: int = 7  # establishes secret number
    x: str = input("Guess a number: ")  # allows user to guess
    print("Your guess was " + x)

    # compares user input to secret number and prints string.
    if int(x) == secret:
        print("You got it!")
    elif int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))

    return None


# calls function
if __name__ == "__main__":
    guess_a_number()
