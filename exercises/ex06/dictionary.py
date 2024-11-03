"""Dictionary for EX06!"""

__author__ = "730762344"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Flips keys and values in input list"""
    output: dict[str, str] = {}
    values: list[str] = []
    i: int = 0
    # creates list of all values in list
    for item in input:
        values.append(input[item])

    # checks that there are no duplicate values in list created
    for i in range(len(values)):
        for x in range(len(values)):
            if values[x] == values[i] and x != i:
                raise KeyError("Duplicate value found!")

    # inverts keys and values
    for key in input:
        output[input[key]] = key

    return output


def favorite_color(favs: dict[str, str]) -> str:
    """Finds most popular favorite color from list"""
    output: str = ""
    colors: list[str] = []
    no_dups: list[str] = []

    # returns empty string if empty dictionary
    if len(favs) == 0:
        return ""

    # creates list of all colors in list
    for item in favs:
        colors.append(favs[item])

    # creates count dictionary to count each color occurence
    counts: dict[str, int] = {}
    for item in colors:
        if item in no_dups:
            counts[item] += 1
        else:
            no_dups.append(item)
            counts[item] = 1

    # finds the most popular color
    greatest: int = 0  # count of most popular color
    output = colors[0]
    for i in counts:
        if counts[i] > greatest:
            output = i
            greatest = counts[i]

    return output


def count(input: list[str]) -> dict[str, int]:
    """counts appearances in input list"""
    output: dict[str, int] = {}

    # loops through list, and adds to count in output dict
    for item in input:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1

    return output


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Assigns each word in list to first letter into dictionary"""
    output: dict[str, list[str]] = {}

    # loops through input list
    for item in input:
        first: str = item[0].lower()  # first letter

        # first time letter is used, creates empty list
        if first not in output:
            output[first] = []
            # append to list in value of output

        # appends item to list value
        output[first].append(item)

    return output


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates dictionary for attendance"""
    if day not in attendance:
        attendance[day] = []  # creates new list for new day
    if student not in attendance[day]:
        attendance[day].append(student)  # adds student if not already there

    return None
