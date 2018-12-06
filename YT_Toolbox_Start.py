import toolbox
from tools.ThumbnailCreator import thumbnailCreatorTool

tb = toolbox.Toolbox()
tct = thumbnailCreatorTool.ThumbnailCreatorTool
for i in range(7):
    tb.add_tool(tct())
tb.run()
