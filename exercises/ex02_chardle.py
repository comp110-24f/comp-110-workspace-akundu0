"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730762344"


# takes user input of word
def input_word() -> str:
    guess: str = input("Enter a 5-character word: ")

    # checks if word has 5 characters
    if len(guess) == 5:
        return guess
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # exits program if input is more than five characters


# takes user input of 1 character
def input_letter() -> str:
    char: str = input("Enter a single character: ")

    # checks if input is 1 character
    if len(char) == 1:
        return char
    else:
        print("Error: Character must be a single character.")
        exit()  # exits program if input is more than one character


# counts and locates instances of the character in the word
def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0

    # checks each index in the word
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    # prints total number of instances of the character in the word.
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
