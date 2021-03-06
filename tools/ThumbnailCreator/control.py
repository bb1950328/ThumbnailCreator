import logging
import sys

from tools.ThumbnailCreator import model, gui


class ThumbnailCreatorControl:
    def __init__(self):
        self.log_formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
        self.logger = logging.getLogger(__name__)
        self.log_file_handler = logging.FileHandler("thumbnail_creator_log.log")
        self.log_file_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(self.log_file_handler)
        self.log_console_handler = logging.StreamHandler(sys.stdout)
        self.log_console_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(self.log_console_handler)
        self.logger.setLevel(logging.DEBUG)
        self.gui = gui.ThumbnailCreatorGUI()
        self.model = model.ThumbnailCreatorModel()
        self.make_bindings()

    def make_bindings(self):
        self.logger.debug("make bindings")
        self.gui.background.filePath.trace("w", self.image_changed)
        self.gui.background.filePathEntry.bind("<Return>", self.image_changed)
        self.gui.root.bind("<Control-MouseWheel>", self.zoom_preview)
        self.gui.root.bind("<Control-Button-4>", self.zoom_preview_up)
        self.gui.root.bind("<Control-Button-5>", self.zoom_preview_down)
        self.gui.background.crop_x1_value.trace("w", self.crop_event)
        self.gui.background.crop_x2_value.trace("w", self.crop_event)
        self.gui.background.crop_y1_value.trace("w", self.crop_event)
        self.gui.background.crop_y2_value.trace("w", self.crop_event)
        self.gui.background.fast_crop_button["command"] = self.fast_crop

        self.gui.stickers.add_button["command"] = self.sticker_add_button_clicked
        self.gui.stickers.delete_button["command"] = self.sticker_delete_button_clicked
        self.gui.stickers.modify_button["command"] = self.sticker_modify_button_clicked
        self.gui.stickers.up_button["command"] = self.sticker_up_button_clicked
        self.gui.stickers.down_button["command"] = self.sticker_down_button_clicked

    def run(self):
        self.logger.info("starting mainloop in gui now.")
        self.gui.root.mainloop()

    def image_changed(self, *args, **kwargs):
        self.logger.info("image changed", args, kwargs)
        success = self.model.set_background_image_path(self.gui.background.filePath.get())
        if success:
            self.gui.background.filePathEntry["fg"] = "green"
            self.refresh_preview()
        else:
            self.gui.background.filePathEntry["fg"] = "red"

    def refresh_preview(self):
        self.gui.preview.set_pil_image(self.model.render())

    def zoom_preview(self, event):
        old_width = int(self.gui.preview.canvas["width"])
        old_height = int(self.gui.preview.canvas["height"])
        if event.delta > 0:
            new_width = old_width * 1.1
            new_height = old_height * 1.1
        else:
            new_width = old_width * 0.9
            new_height = old_height * 0.9

        self.logger.debug("zoom", event.delta, "from", (old_width, old_height), "to", (new_width, new_height))
        img = self.model.render(resize=(int(new_width), int(new_height)))
        self.gui.preview.set_pil_image_without_resize(img)

    def zoom_preview_up(self, event):
        class FakeEvent:
            pass

        fake_event = FakeEvent()
        fake_event.delta = 1
        # noinspection PyTypeChecker
        self.zoom_preview(fake_event)

    def zoom_preview_down(self, event):
        class FakeEvent:
            pass

        fake_event = FakeEvent()
        fake_event.delta = -1
        # noinspection PyTypeChecker
        self.zoom_preview(fake_event)

    def crop_event(self, *args):
        self.logger.info("crop image", args)
        self.model.crop_image(self.gui.background.crop_x1_value.get(),
                              self.gui.background.crop_y1_value.get(),
                              -self.gui.background.crop_x2_value.get(),
                              -self.gui.background.crop_y2_value.get())
        self.refresh_preview()

    def fast_crop(self):
        if self.model.image is None:
            return
        fastcropper = gui.FastCropDialog()
        result = fastcropper.run(self.model.image, self.model.image_crop)
        if result is not None:
            self.model.crop_image(*result)
            self.gui.background.update_crop_fields(result[0], result[1],
                                                   self.model.get_raw_image_size()[0] - result[2],
                                                   self.model.get_raw_image_size()[1] - result[3])
            self.refresh_preview()

    def sticker_add_button_clicked(self, *args):
        # TODO
        self.add_sticker(sticker.TextSticker())
        pass

    def sticker_delete_button_clicked(self, *args):
        # TODO
        pass

    def sticker_modify_button_clicked(self, *args):
        # TODO
        pass

    def sticker_up_button_clicked(self, *args):
        # TODO
        pass

    def sticker_down_button_clicked(self, *args):
        # TODO
        pass


def run():
    control = ThumbnailCreatorControl()
    control.run()
