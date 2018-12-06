import toolbox
from tools.ThumbnailCreator import thumbnailCreatorTool

tb = toolbox.Toolbox()
tct = thumbnailCreatorTool.ThumbnailCreatorTool
tb.add_tool(tct())
tb.run()
