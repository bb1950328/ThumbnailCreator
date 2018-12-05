class Tool:
    def run(self):
        pass

    def get_icon_path(self):
        return None

    def can_run_multiple_instances(self):
        return False

    def can_run(self):
        return False
