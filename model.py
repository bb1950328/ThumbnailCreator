class ThumbnailCreatorModel:
    image_path = ""  # type: str

    def __init__(self):
        pass

    def set_image_path(self, new_path):
        """
        :type new_path: str
        :rtype: None
        """
        self.image_path = new_path
