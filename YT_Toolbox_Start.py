import toolbox
from tools.ThumbnailCreator import thumbnailCreatorTool
from tools.ffmpegGUI import ffmpegGUITool

tools = [thumbnailCreatorTool.ThumbnailCreatorTool, ffmpegGUITool.ffmpegGUITool]

tb = toolbox.Toolbox()
for tool in tools:
    tb.add_tool(tool())
tb.run()
