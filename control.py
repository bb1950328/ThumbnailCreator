import gui
import model


class ThumbnailCreatorControl:
    def __init__(self):
        self.gui = gui.ThumbnailCreatorGUI()
        self.model = model.ThumbnailCreatorModel()
        self.gui.background.filePath.trace("w", self.image_changed)
        self.gui.background.filePathEntry.bind("<Return>", self.image_changed)
        # self.gui.background.path_ok_button["command"] = self.image_changed

    def run(self):
        self.gui.root.mainloop()

    def image_changed(self, *args, **kwargs):
        print("image changed", args, kwargs)
        success = self.model.set_background_image_path(self.gui.background.filePath.get())
        if success:
            self.gui.background.filePathEntry["fg"] = "green"
            self.refresh_preview()
        else:
            self.gui.background.filePathEntry["fg"] = "red"

    def refresh_preview(self):
        self.gui.preview.set_pil_image(self.model.render())


control = ThumbnailCreatorControl()
control.run()
