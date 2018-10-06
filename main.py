from tkinter import *


class ThumbnailCreator:
    def __init__(self):
        self.root = Tk()
        self.root.title("ThumbnailCreator")
        self.preview = ThumbnailCreatorPreview(self.root)
        self.preview.root.pack()  # side="left")
        self.background = ThumbnailCreatorBackground(self.root)
        self.background.root.pack()  # side="top")


class ThumbnailCreatorPreview:
    def __init__(self, parent):
        self.root = LabelFrame(parent)
        self.label = Label(self.root)
        self.label["text"] = "Preview"
        self.root["labelwidget"] = self.label
        # self.root.pack()
        self.canvas = Canvas(self.root)
        self.canvas.pack()


class ThumbnailCreatorBackground:
    def __init__(self, parent):
        self.root = LabelFrame(parent)
        self.label = Label(self.root)
        self.label["text"] = "Image Background"
        self.root["labelwidget"] = self.label
        self.filePathFrame = LabelFrame(self.root)
        self.filePathLabel = Label(self.root)
        self.filePathLabel["text"] = "Image File"
        self.filePathFrame["labelwidget"] = self.filePathLabel
        self.filePathEntry = Entry(self.root)
        self.filePathEntry.pack(side="left")
        self.filePathBrowseButton = Button(self.filePathFrame, text="Browse...", command=self.chooseFile)

    def chooseFile(self):



myCreator = ThumbnailCreator()
myCreator.root.mainloop()
