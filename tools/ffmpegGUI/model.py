import os
import re
import subprocess


class Ffmpeg:
    def __init__(self):
        pass

    def search_for_ffmpeg(self, path):
        """
        :param path: folder to search in
        :return: path of ffmpeg(.exe) or None if there is no ffmpeg(.exe)
        """
        found = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if "ffmpeg" in file:
                    full_path = os.path.join(root, file)
                    if os.access(full_path, os.F_OK | os.R_OK | os.X_OK):
                        found.append(full_path)
                        if self.verify_is_ffmpeg(found[-1]):
                            return found[-1]
        if len(found) == 0:
            return None
        return found[0]

    def verify_is_ffmpeg(self, path):
        """
        :param path: something like "C:\ffmpeg.exe
        :return: boolean
        """
        try:
            out = subprocess.check_output([path, "-version"])
        except OSError:
            return False
        return re.match("ffmpeg version [\\s\\S]*", out)
