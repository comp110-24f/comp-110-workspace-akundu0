"""Turtle art!"""

from .turtle import Turtle
from math import pi

__template__ = "https://24ss2.comp110.com/static/turtle/"


def main() -> Turtle:
    t: Turtle = Turtle()
    t.setSpeed(0.25)
    t.forward(150)
    t.left(pi / 2.0)
    t.forward(140)
    t.left(pi / 2.0)
    return t
