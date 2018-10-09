from enum import Enum


class Align(Enum):
    """
    Enum for specifying Directions
    NW  N   NE
    W   C   E
    SW  S   SE

    boolean operations are supported:
    #TODO
    """
    NORTH = 0b1
    EAST = 0b10
    SOUTH = 0b100
    WEST = 0b1000
    CENTER = 0b10000
    N = NORTH
    E = EAST
    S = SOUTH
    W = WEST
    C = CENTER
    NE = N + E
    SE = S + E
    NW = N + W
    SW = S + W

    def __add__(self, other):


# TODO
class Sticker:
    name = ""
    position = (-1, -1)

    def __init__(self):
        pass

    def render(self):
        pass

    def
