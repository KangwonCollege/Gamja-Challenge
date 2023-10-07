import os

from PIL import Image
from PIL.ImageDraw import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont

from utils.directory import directory


class BaseProfile:
    def __init__(self):
        self.FONT_COLOR = "#FFFFFF"
        self.OUTLINE_COLOR = "#FFFFFF"
        self.CALENDER_COLOR1 = "#39D353"
        self.CALENDER_COLOR2 = "#26A641"
        self.CALENDER_COLOR3 = "#006D32"
        self.CALENDER_COLOR4 = "#0E4429"
        self.CALENDER_COLOR5 = "#2E2E2E"
        self.BACKGROUND_COLOR = "#313338"
        self.BACKGROUND_TIER_COLOR = "#3C3D42"
        self.BACKGROUND_BASE_COLOR = (0, 0, 0, 0)

        self.WIDTH = 500
        self.HEIGHT = 180

        self.user_image: str | Image | None = None

    def base_img(self):
        return Image.new(
            mode="RGBA",
            size=(self.WIDTH, self.HEIGHT),
            color=self.BACKGROUND_BASE_COLOR
        )

    def user_profile(self):
        pass

    def user_calender(self):
        pass
