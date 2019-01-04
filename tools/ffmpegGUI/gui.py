from tkinter import Tk, LabelFrame, Label, Entry, Button, Listbox


class ffmpegGUI:
    def __init__(self):
        pass

    def run(self):
        self.root = Tk()
        self.root.title("ffmpegGUI")

        self.inputframe = LabelFrame(self.root)
        self.inputframeLabel = Label(self.inputframe)
        self.inputframe["labelwidget"] = self.inputframeLabel
        self.inputframeLabel["text"] = "Input"
        self.inputframe.grid(row=0, column=0)

        self.converterframe = LabelFrame(self.root)
        self.converterframeLabel = Label(self.converterframe)
        self.converterframe["labelwidget"] = self.converterframeLabel
        self.converterframeLabel["text"] = "Converter"
        self.converterframe.grid(row=0, column=1)

        self.outputframe = LabelFrame(self.root)
        self.outputframeLabel = Label(self.outputframe)
        self.outputframe["labelwidget"] = self.outputframeLabel
        self.outputframeLabel["text"] = "Output"
        self.outputframe.grid(row=0, column=2)

        self.build_inputframe()
        self.build_converterframe()
        self.build_outputframe()

        self.root.mainloop()

    def build_inputframe(self):
        pass

    def build_converterframe(self):
        self.converter_sourceframe = LabelFrame(self.converterframe)
        self.converter_sourceframeLabel = Label(self.converter_sourceframe)
        self.converter_sourceframeLabel["text"] = "ffmpeg.exe location"
        self.converter_sourceframe["labelwidget"] = self.converter_sourceframeLabel
        self.coverter_sourceEntry = Entry(self.converter_sourceframe)
        self.converter_sourceChangeButton = Button(self.converter_sourceframe, text="Change...")
        self.converter_sourceframe.grid(row=0, column=0)
        self.coverter_sourceEntry.grid(row=0, column=0)
        self.converter_sourceChangeButton.grid(row=1, column=0)

        self.converter_optionsframe = LabelFrame(self.converterframe)
        self.converter_optionsframe.grid(row=1, column=0)
        self.converter_optionsframeLabel = Label(self.converter_optionsframe)
        self.converter_optionsframeLabel["text"] = "commandline options"
        self.converter_optionsframe["labelwidget"] = self.converter_optionsframeLabel
        self.converter_optionslist = Listbox(self.converter_optionsframe)
        self.converter_optionslist.grid(row=0, column=0)
        self.converter_optionslist.insert(0, "test")
        self.converter_optionslist_addButton = Button(self.converter_optionsframe, text="Add...")
        self.converter_optionslist_editButton = Button(self.converter_optionsframe, text="Edit...")
        self.converter_optionslist_deleteButton = Button(self.converter_optionsframe, text="Delete")
        self.converter_optionslist_addButton.grid(row=1, column=0)
        self.converter_optionslist_editButton.grid(row=2, column=0)
        self.converter_optionslist_deleteButton.grid(row=3, column=0)

    def build_outputframe(self):
        pass


def run():
    fg = ffmpegGUI()
    fg.run()
