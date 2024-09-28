"""Importing + Scope"""

__author__ = "730762344"


def get_coords(xs: str, ys: str) -> None:
    i: int = 0  # initializes index for xs
    n: int = 0  # initializes index for ys

    while i < len(xs):
        n = 0  # resets n to 0 after while loop
        while n < len(ys):
            print("(" + xs[i] + "," + ys[n] + ")")  # prints out formatted coordinates
            n += 1  # increases looping variable
        i += 1  # increases looping variable
