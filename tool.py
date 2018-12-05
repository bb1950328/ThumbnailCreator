class Tool:
    def run(self):
        pass

    def get_icon_path(self):
        """
        :return: absolute path of the icon or None if there is no icon
        """
        return None

    def can_run_multiple_instances(self):
        return False

    def can_run(self):
        return False

    def get_description(self):
        return "this is just the parent class for every tool and cannot be runned."

    def get_Name(self):
        return "Tool"
