import random
import tempfile

from PIL import Image


class ThumbnailCreatorModel:
    _image_path = ""  # type: str
    _image_crop = (0, 0, -1, -1)

    def __init__(self):
        pass
        self.image = None

    def set_image_path(self, new_path):
        """
        :type new_path: str
        :rtype: bool
        """
        self._image_path = new_path
        try:
            self.image = Image.open(self._image_path)
        except IOError:
            return False

    def get_raw_image_size(self):
        """
        :return (width, height)
        """
        if self.image is None:
            return None
        return self.image.size

    def get_cropped_image_size(self):
        """
        :return: (width, height)
        """
        if self._image_crop:
            x1, y1, x2, y2 = self._image_crop
            return x2 - x1, y2 - y1
        elif self.image:
            return self.image.size
        else:
            return None

    def crop_image(self, x1, y1, x2, y2):
        """
        :param x1: int
        :param y1: int
        :param x2: int
        :param y2: int
        :raise ValueError
        :return None
        """
        width, height = self.get_raw_image_size()
        if x1 < 0:
            x1 += width
        if x2 < 0:
            x2 += width
        if y1 < 0:
            y1 += height
        if y2 < 0:
            y2 += height

        if x1 > width:
            raise ValueError("x1 too big!")
        if x2 > width:
            raise ValueError("x2 too big!")
        if x1 > x2:
            raise ValueError("x1 > x2")
        if y1 > width:
            raise ValueError("y1 too big!")
        if y2 > width:
            raise ValueError("y2 too big!")
        if y1 > y2:
            raise ValueError("y1 > y2")

        self._image_crop = (x1, y1, x2, y2)

    def render(self, resize=None):
        result = Image.new("RGBA", self.get_cropped_image_size())
        return result

    def render_and_save(self, resize=None, path=None):
        result = self.render(resize)
        if path is None:
            path = tempfile.gettempdir() + "tmp" + hex(random.randint(0x10000, 0xFFFFF))[2:] + ".png"
