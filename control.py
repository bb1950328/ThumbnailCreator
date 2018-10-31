import gui
import model


class ThumbnailCreatorControl:
    def __init__(self):
        self.gui = gui.ThumbnailCreatorGUI()
        self.model = model.ThumbnailCreatorModel()
        self.gui.background.filePath.trace("w", self.image_changed)

    def run(self):
        self.gui.root.mainloop()

    def image_changed(self, *args, **kwargs):
        self.model.set_image_path(self.gui.background.filePath.get())


control = ThumbnailCreatorControl()
control.run()
