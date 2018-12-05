from tkinter import Tk, Frame, Label, messagebox

from PIL import Image, ImageTk

ICONSIZE = 128


class Toolbox:
    def __init__(self):
        self.root = None
        self.toolStarters = []

    def refresh_toolstarters(self):
        width = self.root.winfo_width()
        columns = width / ICONSIZE
        c = r = 0
        for ts in self.toolStarters:
            pass
            # TODO

    def run(self):
        self.root = Tk()
        self.root.title("YT Toolbox")


class ToolStarter:
    def __init__(self, tool):
        self.tool = tool

    def generate_frame(self, root):
        frame = Frame(root)
        filepath = self.tool.get_icon_path()
        img = Image.open(filepath).resize((ICONSIZE, ICONSIZE), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        imglabel = Label(frame, image=img)
        imglabel.pack()
        namelabel = Label(frame, text=self.tool.get_Name())
        namelabel.pack()
        frame.bind("<Button-1>", self.start)
        return frame

    def start(self):
        if not self.tool.can_run():
            messagebox.showerror("Cannot run", "You have too much instances of " + self.tool.get_Name() + " running.")
            return
        self.tool.run()
