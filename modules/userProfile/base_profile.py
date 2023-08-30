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

    def _base(self) -> Image:
        return Image.new(
            mode="RGBA",
            size=(self.WIDTH, self.HEIGHT),
            color=self.BACKGROUND_BASE_COLOR
        )

    def _radius_base(self, base_img: Image = None) -> Image:
        if base_img is None:
            base_img = self._base

        drow_img = ImageDraw(base_img)
        drow_img.rounded_rectangle(
            (0, 0, 500, 180),
            radius=20,
            fill=self.BACKGROUND_COLOR
        )

        return base_img

    def _radius(self, base_img: Image = None) -> Image:
        if base_img is None:
            base_img = self._base

        drow_img = ImageDraw(base_img)
        drow_img.rounded_rectangle(
            (0, 0, 500, 180),
            radius=20,
            outline=self.OUTLINE_COLOR,
            width=3
        )

        return base_img

    @staticmethod
    def font(font_size: int = 18, width: str = "Bold") -> ImageFont:
        return ImageFont.truetype(os.path.join(directory, "assets", f"Inter-{width}.ttf"), font_size)

    def user_profile_canvas(self) -> Image:
        base_img = self._radius_base()
        draw_img = ImageDraw(base_img)
        draw_img.rounded_rectangle(
            xy=(390, 0, 500, 180),
            radius=20,
            fill=self.BACKGROUND_TIER_COLOR,
        )
        draw_img.rectangle(
            xy=(390, 0, 410, 180),
            fill=self.BACKGROUND_TIER_COLOR
        )
        img = self._radius(base_img)

        return img

    @staticmethod
    def _load_tier_img(tier: str = "unrank") -> Image:
        img = Image.open(
                fp=os.path.join(directory, "assets", "tier_img", tier+".png"),
                mode="r"
        )

        return img

    def tier(self, img: Image.Image = None, tier: str = "unrank") -> Image:
        """
        load tier assets and draw base_profile
        :param img: base_image
        :param tier: tierName_cnt ex: bronze_3
        tierName : {unrank, bronze, silver, gold, platinum, diamond}\n
        cnt : {1, 2, 3}
        :return:
        """
        if img is None:
            img = self._radius()
        tier_img = self._load_tier_img(tier=tier)

        alpha_channel = tier_img.split()[3]
        mask = alpha_channel.point(lambda x: 0 if x < 128 else 1, '1')
        img.paste(im=tier_img, box=(413, 43), mask=mask)

        font = self.font(18)
        draw_img = ImageDraw(img)
        draw_img.text(
            xy=(445, 121),
            text=tier,
            fill=self.FONT_COLOR,
            anchor="mm",
            font=font,
            align="center"
        )

        return img

    def draw_text(self, img: Image.Image, text: list[str, str, int, int]) -> Image.Image:
        """
        draw Name, UserID, GitHub Commit cnt, Baekjoon Commit cnt
        :param img:
        :param text: list[Name, UserID, Github Commit CNT, Baekjoon Commit CNT]
        :return:
        """
        draw_img = ImageDraw(img)

        draw_img.text(xy=(159, 44), text=text[0], fill=self.FONT_COLOR, font=self.font(26))
        draw_img.text(xy=(162, 77), text="User ID : " + text[1], fill=self.FONT_COLOR, font=self.font(8))
        draw_img.text(xy=(160, 102), text="Github Commit", fill=self.FONT_COLOR, font=self.font(13))
        draw_img.text(xy=(290, 102), text="Baekjoon", fill=self.FONT_COLOR, font=self.font(13))
        draw_img.text(xy=(160, 122), text=str(text[2]), fill=self.FONT_COLOR, font=self.font(12))
        draw_img.text(xy=(290, 122), text=str(text[3]), fill=self.FONT_COLOR, font=self.font(12))
        return img

    def get_img(self, url: str = None) -> Image:

        return

    def draw_img(self, img_url: str, base_img: Image.Image) -> Image:
        img = self.get_img(img_url)
        mask = Image.new("1", (106, 106), 1)
        base_img.paste(im=img, box=(26, 37), mask=mask)

    @staticmethod
    def antialias(img: Image.Image) -> Image:
        # img.resize(
        #     (self.WIDTH // 2, self.HEIGHT // 2),
        #     reducing_gap=Image.LANCZOS)
        img = img.filter(filter=ImageFilter.BoxBlur(1))
        return img


p = BaseProfile()
im = p.user_profile_canvas
im = p.tier(img=im, tier="bronze_3")
im = p.draw_text(img=im, text=["Mule⸝ဗီူ⸜", "5555", 3, 3])
im.show()
