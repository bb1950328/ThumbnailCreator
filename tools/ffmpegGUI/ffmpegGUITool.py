from threading import Thread

from tool import Tool
from tools.ffmpegGUI import gui


class ffmpegGUITool(Tool):
    def __init__(self, max_running_instances=16):
        self.max_workers = max_running_instances
        self.threads = []

    def can_run_multiple_instances(self):
        return True

    def can_run(self):
        self.threads = [t for t in self.threads if t.is_alive()]
        return len(self.threads) < self.max_workers

    def run(self):
        if not self.can_run():
            raise OverflowError("maximum running instances limit exceeded")
        self.threads.append(Thread(target=gui.run))
        self.threads[-1].start()

    def get_icon_path(self):
        return None

    def get_description(self):
        return "a graphical user interface for ffmpeg"

    def get_Name(self):
        return "ffmpegGUI"

    def get_icon_path(self):
        return None
