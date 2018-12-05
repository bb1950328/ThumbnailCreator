from tkinter import Tk


class Toolbox:
    def __init__(self):
        self.root = None
        self.toolStarters = []

    def run(self):
        self.root = Tk()
        self.root.title("YT Toolbox")


class ToolStarter:
    def __init__(self, tool):
        self.tool = tool

    def generate_frame(self):
        pass
        # TODO
