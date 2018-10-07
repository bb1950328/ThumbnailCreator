import os
from tkinter import *
from tkinter import filedialog


class ThumbnailCreatorGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("ThumbnailCreator")
        self.preview = ThumbnailCreatorPreview(self.root)
        self.preview.root.grid(row=0, column=0)
        self.background = ThumbnailCreatorBackground(self.root)
        self.background.root.grid(row=0, column=1)


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
        self.filePathFrame.grid(row=0, column=0)
        self.filePath = StringVar()
        self.filePathEntry = Entry(self.filePathFrame)
        self.filePathEntry["textvariable"] = self.filePath
        self.filePathEntry.grid(row=0, column=0)
        self.filePathBrowseButton = Button(self.filePathFrame)
        self.filePathBrowseButton["text"] = "Browse..."
        self.filePathBrowseButton["command"] = self.choose_file
        self.filePathBrowseButton.grid(row=0, column=1)

        self.cropFrame = LabelFrame(self.root)
        self.cropLabel = Label(self.root)
        self.cropLabel["text"] = "Crop"
        self.cropFrame["labelwidget"] = self.cropLabel
        self.cropFrame.grid(row=1, column=0)

    def choose_file(self):
        self.filePath.set(filedialog.askopenfilename(initialdir=os.getcwd(), title="Select background image"))
