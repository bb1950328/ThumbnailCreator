import os
from tkinter import *
from tkinter import filedialog, ttk

from PIL import Image as PILImage
from PIL import ImageTk


class ThumbnailCreatorGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("ThumbnailCreator")
        self.preview = ThumbnailCreatorPreview(self.root)
        self.preview.root.grid(row=0, column=0, rowspan=2, sticky=N + E + S + W)
        self.background = ThumbnailCreatorBackground(self.root)
        self.background.root.grid(row=0, column=1, sticky=E + W)
        self.stickers = ThumbnailCreatorStickers(self.root)
        self.stickers.root.grid(row=1, column=1)


class ThumbnailCreatorPreview:
    def __init__(self, parent):
        self.width = 500
        self.image_id = None
        self.root = LabelFrame(parent)
        self.label = Label(self.root)
        self.label["text"] = "Preview"
        self.root["labelwidget"] = self.label
        self.canvas = Canvas(self.root, bg="white")
        self.canvas.pack()

    def set_pil_image(self, image):
        if self.image_id is not None:
            self.canvas.delete(self.image_id)
        wpercent = (self.width / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((self.width, hsize), PILImage.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.image_id = self.canvas.create_image(0, 0, image=photo, anchor=NW)
        self.canvas.update()
        print("updated preview", self.image_id, photo)

    def set_file_image(self, filename):
        pil_image = PILImage.open(filename)
        self.set_pil_image(pil_image)


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

        self.crop_x1_label = Label(self.cropFrame)
        self.crop_x1_label["text"] = "Left"
        self.crop_x1_spinbox = Spinbox(self.cropFrame)
        self.crop_x1_label.grid(column=0, row=0)
        self.crop_x1_spinbox.grid(column=1, row=0)

        self.crop_x2_label = Label(self.cropFrame)
        self.crop_x2_label["text"] = "Right"
        self.crop_x2_spinbox = Spinbox(self.cropFrame)
        self.crop_x2_label.grid(column=0, row=1)
        self.crop_x2_spinbox.grid(column=1, row=1)

        self.crop_y1_label = Label(self.cropFrame)
        self.crop_y1_label["text"] = "Top"
        self.crop_y1_spinbox = Spinbox(self.cropFrame)
        self.crop_y1_label.grid(column=0, row=2)
        self.crop_y1_spinbox.grid(column=1, row=2)

        self.crop_y2_label = Label(self.cropFrame)
        self.crop_y2_label["text"] = "Bottom"
        self.crop_y2_spinbox = Spinbox(self.cropFrame)
        self.crop_y2_label.grid(column=0, row=3)
        self.crop_y2_spinbox.grid(column=1, row=3)

        self.fast_crop_button = Button(self.cropFrame)
        self.fast_crop_button["text"] = "Fast\nCrop"
        self.fast_crop_button.grid(column=2, row=1, rowspan=4)

    def choose_file(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select background image")
        self.filePathEntry.delete(0, END)
        self.filePathEntry.insert(0, filename)


class ThumbnailCreatorStickers:
    def __init__(self, parent):
        self.root = LabelFrame(parent)
        self.root_label = Label(self.root)
        self.root_label["text"] = "Stickers"
        self.root["labelwidget"] = self.root_label

        self.tree = ttk.Treeview(self.root)
        self.add_button = Button(self.root)
        self.add_button["text"] = "Add..."
        self.delete_button = Button(self.root)
        self.delete_button["text"] = "Delete"
        self.modify_button = Button(self.root)
        self.modify_button["text"] = "Modify..."
        self.up_button = Button(self.root)
        self.up_button["text"] = "Up"
        self.down_button = Button(self.root)
        self.down_button["text"] = "Down"

        self.tree.grid(column=0, row=0, columnspan=5)
        self.add_button.grid(column=0, row=1)
        self.delete_button.grid(column=1, row=1)
        self.modify_button.grid(column=2, row=1)
        self.up_button.grid(column=3, row=1)
        self.down_button.grid(column=4, row=1)
