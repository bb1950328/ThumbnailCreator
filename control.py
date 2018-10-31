import gui
import model


class ThumbnailCreatorControl:
    def __init__(self):
        self.gui = gui.ThumbnailCreatorGUI()
        self.model = model.ThumbnailCreatorModel()
        # self.gui.background.filePath.trace("w", lambda *args: self.image_changed())
        self.gui.background.filePathEntry.bind("<Return>", self.image_changed)

    def run(self):
        self.gui.root.mainloop()

    def image_changed(self, *args):
        print("image changed", args)
        self.model.set_image_path(self.gui.background.filePath.get())
        self.refresh_preview()

    def refresh_preview(self):
        self.gui.preview.set_pil_image(self.model.render())

control = ThumbnailCreatorControl()
control.run()
