"""Basic syntax of lists"""

# creating an empty list
my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

# creating empty string
# my_name: str = "" # literal
# my_name: str = str() # constructor

print(my_numbers)

my_numbers.append(1.5)

print(my_numbers)

# subscription notation/indexing
game_points: list[int] = [102, 86, 94]
print(game_points)
print(game_points[2])

game_points[1] = 72
print(game_points)

# getting the length
print(len(game_points))

# removing items
game_points.pop(1)  # shifts the index
print(game_points)


def display(list_ints: list[int]) -> None:
    """Prints each element of a list"""
    i: int = 0
    while i < len(list_ints):
        print(list_ints[i])
        i += 1


display(game_points)

game_points.append(94)
print(game_points)
print(game_points[10])
