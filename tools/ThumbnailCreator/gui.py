import os
import tkinter
from tkinter import filedialog, ttk

from PIL import Image as PILImage
from PIL import ImageTk


class ThumbnailCreatorGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("YT_Toolbox")
        self.menu = ThumbnailCreatorMenu(self.root)
        self.preview = ThumbnailCreatorPreview(self.root)
        self.background = ThumbnailCreatorBackground(self.root)
        self.stickers = ThumbnailCreatorStickers(self.root)
        self.root.configure(menu=self.menu.menubar)
        tkinter.Grid.columnconfigure(self.root, 1, weight=1)
        self.preview.root.grid(row=0, column=0, rowspan=2,
                               sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        self.background.root.grid(row=0, column=1, sticky=tkinter.E + tkinter.W)
        self.stickers.root.grid(row=1, column=1, sticky=tkinter.W + tkinter.E)


class ThumbnailCreatorMenu:
    def __init__(self, parent):
        self.menubar = tkinter.Menu(parent)

        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)

        self.openmenu = tkinter.Menu(self.filemenu, tearoff=0)
        self.openmenu.add_command(label="Image...")
        self.openmenu.add_command(label="Image as Background")
        self.openmenu.add_command(label="Image as Sticker")

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Exit")
        self.filemenu.add_cascade(label="Open...", menu=self.openmenu)
        self.filemenu.add_command(label="Export...")
        self.filemenu.add_command(label="Save as template...")

        self.editmenu = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)


class ThumbnailCreatorPreview:
    def __init__(self, parent):
        self.width = 500
        self.height = None
        self.image_id = None
        self.root = tkinter.LabelFrame(parent)
        self.label = tkinter.Label(self.root)
        self.label["text"] = "Preview"
        self.root["labelwidget"] = self.label
        self.canvas = tkinter.Canvas(self.root, bg="white")
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
        self.image_id = self.canvas.create_image((0, 0), image=photo, anchor=tkinter.NW)
        # self.image_id = self.canvas.create_rectangle(x1=5, x2=10, y1=5, y2=10, fill="red")
        self.canvas.update()
        print("updated preview", self.image_id, photo)

    def set_pil_image_without_resize(self, image):
        photo = ImageTk.PhotoImage(image)
        self.root.photo = photo
        self.width, self.height = image.size
        self.canvas["height"] = self.height
        self.canvas["width"] = self.width
        self.image_id = self.canvas.create_image((0, 0), image=photo, anchor=tkinter.NW)
        # self.image_id = self.canvas.create_rectangle(x1=5, x2=10, y1=5, y2=10, fill="red")
        self.canvas.update()
        print("updated preview raw", self.image_id, photo)

    def set_file_image(self, filename):
        pil_image = PILImage.open(filename)
        self.set_pil_image(pil_image)


class ThumbnailCreatorBackground:
    def __init__(self, parent):
        self.root = tkinter.LabelFrame(parent)
        self.label = tkinter.Label(self.root)
        self.label["text"] = "Image Background"
        self.root["labelwidget"] = self.label

        self.filePathFrame = tkinter.LabelFrame(self.root)
        self.filePathLabel = tkinter.Label(self.root)
        self.filePathLabel["text"] = "Image File"
        self.filePathFrame["labelwidget"] = self.filePathLabel
        self.filePathFrame.grid(row=0, column=0)
        self.filePath = tkinter.StringVar()
        self.filePathEntry = tkinter.Entry(self.filePathFrame)
        self.filePathEntry["textvariable"] = self.filePath
        self.filePathEntry.grid(row=0, column=0)
        self.filePathBrowseButton = tkinter.Button(self.filePathFrame)
        self.filePathBrowseButton["text"] = "Browse..."
        self.filePathBrowseButton["command"] = self.choose_file
        self.filePathBrowseButton.grid(row=0, column=1)

        self.cropFrame = tkinter.LabelFrame(self.root)
        self.cropLabel = tkinter.Label(self.root)
        self.cropLabel["text"] = "Crop"
        self.cropFrame["labelwidget"] = self.cropLabel
        self.cropFrame.grid(row=1, column=0)

        self.crop_x1_label = tkinter.Label(self.cropFrame)
        self.crop_x1_label["text"] = "Left"
        self.crop_x1_value = tkinter.IntVar()
        self.crop_x1_value.set(0)
        self.crop_x1_spinbox = tkinter.Spinbox(self.cropFrame,
                                               textvariable=self.crop_x1_value,
                                               from_=0, to_=10000)
        self.crop_x1_label.grid(column=0, row=0)
        self.crop_x1_spinbox.grid(column=1, row=0)

        self.crop_x2_label = tkinter.Label(self.cropFrame)
        self.crop_x2_label["text"] = "Right"
        self.crop_x2_value = tkinter.IntVar()
        self.crop_x2_value.set(0)
        self.crop_x2_spinbox = tkinter.Spinbox(self.cropFrame,
                                               textvariable=self.crop_x2_value,
                                               from_=0, to_=10000)
        self.crop_x2_label.grid(column=0, row=1)
        self.crop_x2_spinbox.grid(column=1, row=1)

        self.crop_y1_label = tkinter.Label(self.cropFrame)
        self.crop_y1_label["text"] = "Top"
        self.crop_y1_value = tkinter.IntVar()
        self.crop_y1_value.set(0)
        self.crop_y1_spinbox = tkinter.Spinbox(self.cropFrame,
                                               textvariable=self.crop_y1_value,
                                               from_=0, to_=10000)
        self.crop_y1_label.grid(column=0, row=2)
        self.crop_y1_spinbox.grid(column=1, row=2)

        self.crop_y2_label = tkinter.Label(self.cropFrame)
        self.crop_y2_label["text"] = "Bottom"
        self.crop_y2_value = tkinter.IntVar()
        self.crop_y2_value.set(0)
        self.crop_y2_spinbox = tkinter.Spinbox(self.cropFrame,
                                               textvariable=self.crop_y2_value,
                                               from_=0, to_=10000)
        self.crop_y2_label.grid(column=0, row=3)
        self.crop_y2_spinbox.grid(column=1, row=3)

        self.fast_crop_button = tkinter.Button(self.cropFrame)
        self.fast_crop_button["text"] = "Fast\nCrop"
        self.fast_crop_button.grid(column=2, row=1, rowspan=4)

    def update_crop_fields(self, x1, y1, x2, y2):
        self.crop_x1_value.set(x1)
        self.crop_y1_value.set(y1)
        self.crop_x2_value.set(x2)
        self.crop_y2_value.set(y2)

    def choose_file(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="Select background image")
        self.filePathEntry.delete(0, tkinter.END)
        self.filePathEntry.insert(0, filename)


class ThumbnailCreatorStickers:
    def __init__(self, parent):
        self.root = tkinter.LabelFrame(parent)
        self.root_label = tkinter.Label(self.root)
        self.root_label["text"] = "Stickers"
        self.root["labelwidget"] = self.root_label
        for c in range(5):
            self.root.grid_columnconfigure(c, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        columns = ["Name", "Type", "Size", "Position"]
        self.treeframe = tkinter.Frame(self.root)
        self.treeframe.grid_columnconfigure(0, weight=1)
        self.tree = ttk.Treeview(self.treeframe, columns=columns)
        self.tree_xsb = ttk.Scrollbar(self.treeframe, orient='horizontal', command=self.tree.xview)
        self.tree_ysb = ttk.Scrollbar(self.treeframe, orient='vertical', command=self.tree.yview)
        self.tree_xsb.grid(row=1, column=0, sticky=tkinter.E + tkinter.W)
        self.tree_ysb.grid(row=0, column=1, sticky=tkinter.N + tkinter.S)
        for ih in range(len(columns)):
            self.tree.heading("#" + str(ih), text=columns[ih])
            self.tree.column(columns[ih], stretch=True, width=32)
        self.tree.grid(row=0, column=0, sticky=tkinter.E + tkinter.W)

        self.add_button = tkinter.Button(self.root)
        self.add_button["text"] = "Add..."
        self.add_button["padx"] = 5
        self.delete_button = tkinter.Button(self.root)
        self.delete_button["text"] = "Delete"
        self.delete_button["padx"] = 5
        self.modify_button = tkinter.Button(self.root)
        self.modify_button["text"] = "Modify..."
        self.modify_button["padx"] = 5
        self.up_button = tkinter.Button(self.root)
        self.up_button["text"] = "Up"
        self.up_button["padx"] = 5
        self.down_button = tkinter.Button(self.root)
        self.down_button["text"] = "Down"
        self.down_button["padx"] = 5

        self.treeframe.grid(column=0, row=0, columnspan=5, sticky=tkinter.E + tkinter.W)
        self.add_button.grid(column=0, row=1, sticky=tkinter.E + tkinter.W)
        self.delete_button.grid(column=1, row=1, sticky=tkinter.E + tkinter.W)
        self.modify_button.grid(column=2, row=1, sticky=tkinter.E + tkinter.W)
        self.up_button.grid(column=3, row=1, sticky=tkinter.E + tkinter.W)
        self.down_button.grid(column=4, row=1, sticky=tkinter.E + tkinter.W)

        self.add_button["command"] = self.add_button_clicked
        self.delete_button["command"] = self.delete_button_clicked
        self.modify_button["command"] = self.modify_button_clicked
        self.up_button["command"] = self.up_button_clicked
        self.down_button["command"] = self.down_button_clicked

    def get_selected_indexes(self):
        # TODO
        n = self.tree

    def add_button_clicked(self, *args):
        # TODO
        pass

    def delete_button_clicked(self, *args):
        # TODO
        pass

    def modify_button_clicked(self, *args):
        # TODO
        pass

    def up_button_clicked(self, *args):
        # TODO
        pass

    def down_button_clicked(self, *args):
        # TODO
        pass


class FastCropDialog:
    def run(self, image, existing_crop=None):
        self.backup_crop = existing_crop
        self.width = 1000
        self.root = tkinter.Toplevel()
        self.root.wm_title("Fast Crop Backgrounnd Image")
        self.image = image
        w, h = self.image.size
        self.scale = w / self.width
        self.height = int(h / self.scale)
        self.canvas = tkinter.Canvas(self.root, width=self.width, height=self.height)
        self.ok_button = tkinter.Button(self.root, text="OK")
        self.cancel_button = tkinter.Button(self.root, text="Cancel")
        self.canvas.pack(side=tkinter.TOP)
        self.ok_button.pack(side=tkinter.RIGHT)
        self.cancel_button.pack(side=tkinter.RIGHT)

        self.ok_button["command"] = self.ok_event
        self.cancel_button["command"] = self.cancel_event
        self.root.protocol("WM_DELETE_WINDOW", self.cancel_event)

        self.canvas.bind("<Motion>", self.mouse_moved_event)
        self.canvas.bind("<Button-1>", self.mouse_pressed_event)
        self.canvas.bind("<B1-Motion>", self.mouse_dragged_event)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_released_event)

        self.dragtype = None
        if existing_crop is not None:
            self.actual_crop = tuple(map(int, self.image_xy_to_canvas_xy(*existing_crop)))
        else:
            self.actual_crop = (0, 0, *tuple(map(int, self.image_xy_to_canvas_xy(*image.size))))
        print("actual crop", self.actual_crop, "scale: ", self.scale)
        self.photoimage = ImageTk.PhotoImage(self.image.resize((self.width, self.height)))
        print(w, h, self.photoimage.width(), self.photoimage.height(), self.canvas.size())
        self.image_id = self.canvas.create_image((0, 0), image=self.photoimage, anchor=tkinter.NW)
        self.rect_id1 = None
        self.rect_id2 = None
        self.refresh_rect()
        self.canvas.update()
        self.root.mainloop()
        if self.actual_crop is None:
            print("user canceled cropping")
            return self.backup_crop
        good_crop = tuple(map(int, self.canvas_xy_to_image_xy(*self.actual_crop)))
        print("user confirmed cropping to", good_crop)
        return good_crop

    def ok_event(self):
        self.root.destroy()
        self.root.quit()

    def cancel_event(self):
        self.actual_crop = None
        self.root.destroy()
        self.root.quit()

    def mouse_on_spot(self, event):
        """
        :param event: event objext with x and y
        :return: int
           |     |
        ---5--3--7--
           |     |
           1     2
           |     |
        ---6--4--8--
           |     |
        """
        on_x1 = abs(event.x - self.actual_crop[0]) < 5
        on_y1 = abs(event.y - self.actual_crop[1]) < 5
        on_x2 = abs(event.x - self.actual_crop[2]) < 5
        on_y2 = abs(event.y - self.actual_crop[3]) < 5
        if not any((on_x1, on_y1, on_x2, on_y2)):
            return None
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
        spot = self.mouse_on_spot(event)
        if spot is None:
            self.canvas.config(cursor="")
        elif spot == 1:
            self.canvas.config(cursor="left_side")
        elif spot == 2:
            self.canvas.config(cursor="right_side")
        elif spot == 3:
            self.canvas.config(cursor="top_side")
        elif spot == 4:
            self.canvas.config(cursor="bottom_side")
        elif spot == 5:
            self.canvas.config(cursor="top_left_corner")
        elif spot == 6:
            self.canvas.config(cursor="bottom_left_corner")
        elif spot == 7:
            self.canvas.config(cursor="top_right_corner")
        elif spot == 8:
            self.canvas.config(cursor="bottom_right_corner")

    def mouse_pressed_event(self, event):
        on_spot = self.mouse_on_spot(event)
        print("mouse pressed, spot=", on_spot)
        if on_spot is None:
            self.dragtype = -1
        else:
            self.dragtype = on_spot
        self.drag_start = (event.x, event.y)

    def mouse_dragged_event(self, event):
        print("type=", self.dragtype)
        self.actual_crop = list(self.actual_crop)  # enable assignment
        if self.dragtype == -1:
            return
        elif self.dragtype == 1:
            self.actual_crop[0] = event.x
        elif self.dragtype == 2:
            self.actual_crop[2] = event.x
        elif self.dragtype == 3:
            self.actual_crop[1] = event.y
        elif self.dragtype == 4:
            self.actual_crop[3] = event.y

        elif self.dragtype == 5:
            self.actual_crop[0] = event.x
            self.actual_crop[1] = event.y
        elif self.dragtype == 6:
            self.actual_crop[0] = event.x
            self.actual_crop[3] = event.y
        elif self.dragtype == 7:
            self.actual_crop[2] = event.x
            self.actual_crop[1] = event.y
        elif self.dragtype == 8:
            self.actual_crop[2] = event.x
            self.actual_crop[3] = event.y
        self.actual_crop = tuple(self.actual_crop)
        self.check_actual_crop()
        self.refresh_rect()

    def mouse_released_event(self, event):
        self.dragtype = -1

    def canvas_xy_to_image_xy(self, *canvas_coords):
        image_coords = []
        for i in canvas_coords:
            image_coords.append(i * self.scale)
        return image_coords

    def image_xy_to_canvas_xy(self, *image_coords):
        canvas_coords = []
        for i in image_coords:
            canvas_coords.append(i / self.scale)
        return canvas_coords

    def check_actual_crop(self):
        print(self.actual_crop)
        if self.actual_crop[0] >= self.actual_crop[2]:  # x1 >= x2
            self.actual_crop[0] = self.actual_crop[2] - 5
        if self.actual_crop[1] >= self.actual_crop[3]:  # y1 >= y2
            self.actual_crop[1] = self.actual_crop[3] - 5

    def refresh_rect(self):
        if self.rect_id1 is None:
            self.rect_id1 = self.canvas.create_rectangle(*self.actual_crop,
                                                         outline="black", dash=(8, 8))
        else:
            self.canvas.coords(self.rect_id1,
                               self.actual_crop[0], self.actual_crop[1],
                               self.actual_crop[2], self.actual_crop[3])
        if self.rect_id2 is None:
            self.rect_id2 = self.canvas.create_rectangle(*self.actual_crop,
                                                         outline="white", dash=(8, 8),
                                                         dashoff=8)
        else:
            self.canvas.coords(self.rect_id2,
                               self.actual_crop[0], self.actual_crop[1],
                               self.actual_crop[2], self.actual_crop[3])
        self.canvas.update()
