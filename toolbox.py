from tkinter import Tk, Frame, Label, messagebox, LabelFrame

from PIL import Image, ImageTk

ICONSIZE = 128


class Toolbox:
    def __init__(self):
        self.root = None
        self.toolStarters = []
        self.toolframes = []
        self.lastwidth = self.lastheight = -1

    def refresh_frames(self, *args):
        if len(self.toolStarters) != len(self.toolframes):
            self.toolframes = []
            for ts in self.toolStarters:
                self.toolframes.append(ts.generate_frame(self.root))

    def regrid_toolstarters(self, *args):
        print("called refresh_toolstarters()")
        self.refresh_frames()
        width = self.root.winfo_width()
        columns = int(width / ICONSIZE)
        if columns < 1:
            columns = 1

        c = r = 0
        print("number of frames: ", len(self.toolframes))
        for fr in self.toolframes:
            fr.grid(column=c, row=r)
            c += 1
            if c == columns:
                r += 1
                c = 0

    def configured_event(self, *args):
        print("configured_event called", args)
        nowwidth, nowheight = self.root.winfo_width(), self.root.winfo_height
        if nowwidth != self.lastwidth or nowheight != self.lastheight:  # window was resized
            print("window was resized")
            self.lastwidth, self.lastheight = nowwidth, nowheight
            self.regrid_toolstarters()

    def run(self):
        self.root = Tk()
        self.root.title("YT Toolbox")
        self.regrid_toolstarters()
        self.root.bind("<Configure>", self.configured_event)
        self.root.mainloop()

    def add_tool(self, tool):
        self.toolStarters.append(ToolStarter(tool))


class ToolStarter:
    def __init__(self, tool):
        self.tool = tool

    def generate_frame(self, root):
        frame = LabelFrame(root)
        filepath = self.tool.get_icon_path()
        if filepath is None:
            filepath = "./resources/no_icon_found.png"
        img = Image.open(filepath).resize((ICONSIZE, ICONSIZE), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        imglabel = Label(frame, image=img)
        imglabel.image = img
        imglabel.pack()
        namelabel = Label(frame, text=self.tool.get_Name())
        namelabel.pack()
        imglabel.bind("<Button-1>", self.start)
        return frame

    def start(self, *args):
        if not self.tool.can_run():
            messagebox.showerror("Cannot run", "You have too much instances of " + self.tool.get_Name() + " running.")
            return
        self.tool.run()
