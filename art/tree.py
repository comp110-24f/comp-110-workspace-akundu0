"""Turtle art!"""

from .turtle import Turtle
from math import pi

__template__ = "https://24ss2.comp110.com/static/turtle/"

DEGREE: float = -pi / 180.0  # Constant


def click(x: float, y: float) -> Turtle:
    """Moves turtle to wherever we click on the canvas + draws line!"""
    t: Turtle = Turtle()
    t.moveTo(x, y)
    t.turnTo(90 * DEGREE)
    t.forward(100)
    return t


def branch(t: Turtle, length: float, angle: float) -> None:
    t.turnTo(angle)
    t.forward(length)
    if length > 3.0:
        branch(t, length * 0.75, angle + 335.0 * DEGREE)
    t.turnTo(angle + pi)
    t.forward(length)
    return None
