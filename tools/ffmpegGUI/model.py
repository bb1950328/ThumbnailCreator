import os


class Ffmpeg:
    def __init__(self):
        pass

    def search_for_ffmpeg_exe(self, path):
        """
        :param path: folder to search in
        :return: path of ffmpeg.exe or None if there is no ffmpeg.exe
        """
        found = []
        for root, dirs, files in os.walk('python/Lib/email'):
            if "ffmpeg.exe" in files:
                found.append(root + "ffmpeg.exe")
                if self.verify_is_ffmpeg_exe(found[-1]):
                    return found[-1]
        if len(found) == 0:
            return None
        return found[0]

    def verify_is_ffmpeg_exe(self, path):
        return True
