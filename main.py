from tkinter import *


class ThumbnailCreator:
    def __init__(self):
        self.root = Tk()
        self.root.title("ThumbnailCreator")
        self.preview = ThumbnailCreatorPreview(self.root)


class ThumbnailCreatorPreview:
    def __init__(self, parent):
        self.root = LabelFrame(parent)
        self.label = Label(self.root)
        self.label["text"] = "Preview"
        self.root["labelwidget"] = self.label
        self.root.pack()
        self.canvas = Canvas(self.root)
        self.root.pack()
        self.canvas.pack()


myCreator = ThumbnailCreator()
myCreator.root.mainloop()
