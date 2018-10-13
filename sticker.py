from enum import Enum
from PIL import Image, ImageDraw, ImageFont


class Align(Enum):
    """
    Enum for specifying Directions
    NW  N   NE
    W   C   E
    SW  S   SE
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
    NE = 0b11
    SE = 0b110
    NW = 0b1001
    SW = 0b1100


class Sticker:
    name = ""
    position = (-1, -1)
    align = Align.CENTER

    def __init__(self):
        pass

    def render(self):
        pass


class TextSticker(Sticker):
    text = ""
    font = None
    size = 0

    def __init__(self):
        super().__init__()
