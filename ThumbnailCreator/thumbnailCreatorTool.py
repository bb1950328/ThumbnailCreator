from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from tool import Tool
from ThumbnailCreator import control


class ThumbnailCreatorTool(Tool):
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
        self.threads.append(Thread(target=control.run))
        self.threads[-1].start()

    def get_icon_path(self):
        return None
