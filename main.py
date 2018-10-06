from tkinter import *

root = Tk()
previewFrame = LabelFrame(root)
previewLabel = Label(previewFrame)
previewLabel["text"] = "Preview"
previewFrame["labelwidget"] = previewLabel
previewFrame.pack()
previewCanvas = Canvas(previewFrame)
previewCanvas.pack()
root.mainloop()
