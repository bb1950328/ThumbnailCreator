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
        self.background = ThumbnailCreatorBackground(self.root)
        self.stickers = ThumbnailCreatorStickers(self.root)
        self.preview.root.grid(row=0, column=0, rowspan=2, sticky=N + E + S + W)
        self.background.root.grid(row=0, column=1, sticky=E + W)
        self.stickers.root.grid(row=1, column=1, sticky=W + E)


class ThumbnailCreatorPreview:
    def __init__(self, parent):
        self.width = 500
        self.height = None
        self.image_id = None
        self.root = LabelFrame(parent)
        self.label = Label(self.root)
        self.label["text"] = "Preview"
        self.root["labelwidget"] = self.label
        self.canvas = Canvas(self.root, bg="white")
        self.canvas.pack()

    def clear(self):
        if self.image_id is not None:
            self.canvas.delete(self.image_id)
            self.canvas.update()
            print("cleared preview")

    def set_pil_image(self, image):
        wpercent = (self.width / float(image.size[0]))
        self.height = int(float(image.size[1]) * wpercent)
        print(self.width, self.height, image.size)
        image = image.resize((self.width, self.height), PILImage.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.root.photo = photo
        self.canvas["height"] = self.height
        self.canvas["width"] = self.width
        self.image_id = self.canvas.create_image((0, 0), image=photo, anchor=NW)
        # self.image_id = self.canvas.create_rectangle(x1=5, x2=10, y1=5, y2=10, fill="red")
        self.canvas.update()
        print("updated preview", self.image_id, photo)

    def set_pil_image_without_resize(self, image):
        photo = ImageTk.PhotoImage(image)
        self.root.photo = photo
        self.width, self.height = image.size
        self.canvas["height"] = self.height
        self.canvas["width"] = self.width
        self.image_id = self.canvas.create_image((0, 0), image=photo, anchor=NW)
        # self.image_id = self.canvas.create_rectangle(x1=5, x2=10, y1=5, y2=10, fill="red")
        self.canvas.update()
        print("updated preview raw", self.image_id, photo)

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
        self.crop_x1_value = IntVar()
        self.crop_x1_value.set(0)
        self.crop_x1_spinbox = Spinbox(self.cropFrame, textvariable=self.crop_x1_value, from_=0, to_=10000)
        self.crop_x1_label.grid(column=0, row=0)
        self.crop_x1_spinbox.grid(column=1, row=0)

        self.crop_x2_label = Label(self.cropFrame)
        self.crop_x2_label["text"] = "Right"
        self.crop_x2_value = IntVar()
        self.crop_x2_value.set(0)
        self.crop_x2_spinbox = Spinbox(self.cropFrame, textvariable=self.crop_x2_value, from_=0, to_=10000)
        self.crop_x2_label.grid(column=0, row=1)
        self.crop_x2_spinbox.grid(column=1, row=1)

        self.crop_y1_label = Label(self.cropFrame)
        self.crop_y1_label["text"] = "Top"
        self.crop_y1_value = IntVar()
        self.crop_y1_value.set(0)
        self.crop_y1_spinbox = Spinbox(self.cropFrame, textvariable=self.crop_y1_value, from_=0, to_=10000)
        self.crop_y1_label.grid(column=0, row=2)
        self.crop_y1_spinbox.grid(column=1, row=2)

        self.crop_y2_label = Label(self.cropFrame)
        self.crop_y2_label["text"] = "Bottom"
        self.crop_y2_value = IntVar()
        self.crop_y2_value.set(0)
        self.crop_y2_spinbox = Spinbox(self.cropFrame, textvariable=self.crop_y2_value, from_=0, to_=10000)
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
        self.add_button["padx"] = 5
        self.delete_button = Button(self.root)
        self.delete_button["text"] = "Delete"
        self.delete_button["padx"] = 5
        self.modify_button = Button(self.root)
        self.modify_button["text"] = "Modify..."
        self.modify_button["padx"] = 5
        self.up_button = Button(self.root)
        self.up_button["text"] = "Up"
        self.up_button["padx"] = 5
        self.down_button = Button(self.root)
        self.down_button["text"] = "Down"
        self.down_button["padx"] = 5

        self.tree.grid(column=0, row=0, columnspan=5, sticky=N + E + S + W)
        self.add_button.grid(column=0, row=1)
        self.delete_button.grid(column=1, row=1)
        self.modify_button.grid(column=2, row=1)
        self.up_button.grid(column=3, row=1)
        self.down_button.grid(column=4, row=1)


class FastCropDialog:
    def run(self, image, existing_crop=None):
        self.root = Tk()
        self.root.wm_title("Fast Crop Backgrounnd Image")
        self.canvas = Canvas(self.root)
        self.ok_button = Button(self.root, text="OK")
        self.cancel_button = Button(self.root, text="Cancel")
        self.canvas.pack(side=TOP)
        self.ok_button.pack(side=RIGHT)
        self.cancel_button.pack(side=RIGHT)
        self.ok_button["command"] = self.ok_event
        self.cancel_button["command"] = self.cancel_event
        self.canvas.bind("<Motion>", self.mouse_moved_event)
        self.dragtype = None
        if existing_crop is not None:
            self.actual_crop = existing_crop
        else:
            self.actual_crop = (0, 0, *image.size)
        self.image = image
        self.root.mainloop()
        return self.actual_crop

    def ok_event(self):
        self.root.destroy()
        self.root.quit()

    def cancel_event(self):
        self.actual_crop = None
        self.root.destroy()
        self.root.quit()

    def mouse_on_spot(self, event):
        on_x1 = abs(event.x - self.actual_crop[0]) < 5
        on_y1 = abs(event.y - self.actual_crop[1]) < 5
        on_x2 = abs(event.x - self.actual_crop[2]) < 5
        on_y2 = abs(event.y - self.actual_crop[3]) < 5
        if not any((on_x1, on_y1, on_x2, on_y2)):
            return None
            print("not on line", (event.x, event.y))
        else:
            print("mouse on line", (on_x1, on_y1, on_x2, on_y2), (event.x, event.y))
        if on_x1 and not on_y1 and not on_y2:  # left line
            return 1
        elif on_x2 and not on_y1 and not on_y2:  # right line
            return 2
        elif on_y1 and not on_x1 and not on_x2:  # top line
            return 3
        elif on_y2 and not on_x1 and not on_x2:  # bottom line
            return 4

        elif on_x1 and on_y1:  # top left corner
            return 5
        elif on_x1 and on_y2:  # bottom left corner
            return 6
        elif on_x2 and on_y1:  # top right corner
            return 7
        elif on_x2 and on_y2:  # bottom right corner
            return 8
        return None

    def mouse_moved_event(self, event):
        """on_x1 = abs(event.x - self.actual_crop[0]) < 5
        on_y1 = abs(event.y - self.actual_crop[1]) < 5
        on_x2 = abs(event.x - self.actual_crop[2]) < 5
        on_y2 = abs(event.y - self.actual_crop[3]) < 5
        if not any((on_x1, on_y1, on_x2, on_y2)):
            self.canvas.config(cursor="")
            print("not on line", (event.x, event.y))
        else:
            print("mouse on line", (on_x1, on_y1, on_x2, on_y2), (event.x, event.y))
        if on_x1 and not on_y1 and not on_y2:  # left line
            self.canvas.config(cursor="left_side")
        elif on_x2 and not on_y1 and not on_y2:  # right line
            self.canvas.config(cursor="right_side")
        elif on_y1 and not on_x1 and not on_x2:  # top line
            self.canvas.config(cursor="top_side")
        elif on_y2 and not on_x1 and not on_x2:  # bottom line
            self.canvas.config(cursor="bottom_side")

        elif on_x1 and on_y1:  # top left corner
            self.canvas.config(cursor="top_left_corner")
        elif on_x1 and on_y2:  # bottom left corner
            self.canvas.config(cursor="bottom_left_corner")
        elif on_x2 and on_y1:  # top right corner
            self.canvas.config(cursor="top_right_corner")
        elif on_x2 and on_y2:  # bottom right corner
            self.canvas.config(cursor="bottom_right_corner")"""
        spot = self.mouse_on_spot(event)
        if spot is None:
            self.canvas.config(cursor="")
            print("not on line", (event.x, event.y))
        elif spot == 1:
            self.canvas.config(cursor="left_side")
        elif spot == 2:
            self.canvas.config(cursor="right_side")
        # TODO

    def mouse_pressed_event(self, event):
        pass

    def mouse_dragged_event(self, event):
        pass

    def mouse_released_event(self, event):
        pass
