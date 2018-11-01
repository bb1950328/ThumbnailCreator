from enum import Enum


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
    name = None
    position = None
    size = None
    rotation = 0  # like a clock 0 is normal, 90 is 90degrees to left
    align = Align.CENTER

    def __init__(self):
        pass

    def render(self):
        pass

    def set_position(self, x, y, align=None):
        self.position = (x, y)
        if align is not None:
            self.align = align

    def get_position(self):
        return self.position

    def get_topleft_position(self):
        if self.position is None:
            return None
        if self.align == Align.NW:
            return self.position
        tl_pos = self.position
        if self.align.value & Align.SOUTH:
            tl_pos[1] -= self.size[1]
        elif not (self.align.value & Align.NORTH):
            tl_pos[1] -= self.size[1] / 2

        if self.align.value & Align.EAST:
            tl_pos[0] -= self.size[0]
        if not (self.align.value & Align.WEST):
            tl_pos[0] -= self.size[0] / 2
        return tl_pos


class TextSticker(Sticker):
    text = None
    font = None
    size = 0

    def __init__(self):
        super().__init__()

    def render(self):
        pass


class ImageSticker(Sticker):
    imagePath = None
    image = None
