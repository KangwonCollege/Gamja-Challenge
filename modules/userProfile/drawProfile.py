import os
import random

from PIL import Image
from PIL.ImageDraw import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont

from models.database.userCalender import UserCalender

from utils.directory import directory


class DrawProfile:
    def __init__(self, scope: int = 2):
        self.FONT_COLOR = "#FFFFFF"
        self.FONT_COLOR_SUB = "#98999B"
        self.OUTLINE_COLOR = "#FFFFFF"
        self.CALENDER_COLOR1 = "#39D353"
        self.CALENDER_COLOR2 = "#26A641"
        self.CALENDER_COLOR3 = "#006D32"
        self.CALENDER_COLOR4 = "#0E4429"
        self.CALENDER_COLOR5 = "#2E2E2E"
        self.BACKGROUND_COLOR = "#313338"
        self.BACKGROUND_TIER_COLOR = "#3C3D42"
        self.BACKGROUND_BASE_COLOR = "#313338"

        self.GRASS_1 = "#1EE740"
        self.GRASS_2 = "#26A641"
        self.GRASS_3 = "#006D32"
        self.GRASS_4 = "#0E4429"
        self.GRASS_5 = "#161B22"

        self.scope = scope
        self.WIDTH = 500 * scope
        self.HEIGHT = 180 * scope

        self.user_image: str | Image | None = None

    def _base_img(self) -> Image.Image:
        return Image.new(
            mode="RGBA",
            size=(self.WIDTH, self.HEIGHT),
            color=self.BACKGROUND_BASE_COLOR
        )

    @staticmethod
    def _round_img(im: Image.Image, round_radius: int = 8) -> Image.Image:
        image = Image.new(
            mode="1",
            size=im.size
        )
        mask_img = ImageDraw(image)
        mask_img.rounded_rectangle(xy=((0, 0), im.size), radius=round_radius, fill=1)

        return image

    @staticmethod
    def _blur_img(im: Image.Image, blur: int = 4) -> Image.Image:
        blur_img = im.filter(ImageFilter.BoxBlur(blur))
        return blur_img

    def user_profile(
            self,
            user_name: str = "UserName",
            user_id: str = "0000000000",
            git_commit: str = "NnN",
            solved_commit: str = "NnN",
            tier_name: str = "Unknown",
            season: str = "Season 1",
    ) -> Image.Image:
        image = self._base_img()
        font_name = ImageFont.truetype(os.path.join(directory, "assets", "Inter-Bold.ttf"), size=28 * self.scope)
        font_sub1 = ImageFont.truetype(os.path.join(directory, "assets", "Pretendard-Regular.ttf"), size=8 * self.scope)
        font_sub2 = ImageFont.truetype(os.path.join(directory, "assets", "Inter-Bold.ttf"), size=13 * self.scope)
        font_sub3 = ImageFont.truetype(os.path.join(directory, "assets", "Pretendard-Regular.ttf"), size=12 * self.scope)
        profile_img = Image.open(os.path.join(directory, "assets", "tier_img", "gold_1.png"))
        profile_img.resize(size=(profile_img.size[0] * self.scope, profile_img.size[1] * self.scope))

        draw_img = ImageDraw(image)

        draw_img.rectangle(
            xy=(
                (399 * self.scope - 20, 0 + 20),
                (399 * self.scope - 20 + 121 * self.scope - 40, 0 + 20 + 186 * self.scope - 50)
            ),
            fill=self.BACKGROUND_TIER_COLOR
        )

        draw_img.text(
            xy=(154*self.scope, 43*self.scope),
            text=user_name,
            font=font_name
        )
        draw_img.text(
            xy=(154 * self.scope, 80 * self.scope),
            text=f"UserID : {user_id}",
            font=font_sub1,
            fill=self.FONT_COLOR_SUB
        )

        draw_img.text(
            xy=(154 * self.scope, 104 * self.scope),
            text="Github Commit",
            font=font_sub2,
            fill=self.FONT_COLOR
        )

        draw_img.text(
            xy=(154 * self.scope, 128 * self.scope),
            text=f"{git_commit} Commit",
            font=font_sub3,
            fill=self.FONT_COLOR
        )

        draw_img.text(
            xy=(283 * self.scope, 104 * self.scope),
            text="Baekjoon",
            font=font_sub2,
            fill=self.FONT_COLOR
        )

        draw_img.text(
            xy=(283 * self.scope, 128 * self.scope),
            text=f"{solved_commit} Solved",
            font=font_sub3,
            fill=self.FONT_COLOR
        )

        draw_img.text(
            xy=(435 * self.scope - 50, 109 * self.scope),
            text=tier_name,
            font=font_sub2,
            fill=self.FONT_COLOR
        )

        draw_img.text(
            xy=(436 * self.scope - 40, 132 * self.scope),
            text=season,
            font=font_sub3,
            fill=self.FONT_COLOR
        )

        draw_img.rectangle(
            xy=((20*self.scope + 20, 40*self.scope), (20*self.scope+106*self.scope + 20, 40*self.scope+106*self.scope)),
            fill=self.OUTLINE_COLOR, width=5
        )

        draw_img.rectangle(
            xy=(20, 20, self.WIDTH - 20, self.HEIGHT - 20),
            outline=self.OUTLINE_COLOR,
            width=2
        )

        image.paste(im=profile_img, box=(427*self.scope - 35, 40*self.scope), mask=profile_img.split()[3])

        return image

    def user_calender(self, date_model: UserCalender = None) -> Image.Image:
        grass = [
            Image.new("RGBA", color=self.GRASS_1, size=(12*self.scope, 12*self.scope)),
            Image.new("RGBA", color=self.GRASS_2, size=(12 * self.scope, 12 * self.scope)),
            Image.new("RGBA", color=self.GRASS_3, size=(12 * self.scope, 12 * self.scope)),
            Image.new("RGBA", color=self.GRASS_4, size=(12 * self.scope, 12 * self.scope)),
            Image.new("RGBA", color=self.GRASS_5, size=(12 * self.scope, 12 * self.scope))
        ]

        font_name = ImageFont.truetype(os.path.join(directory, "assets", "Inter-Bold.ttf"), size=28 * self.scope)
        image = self._base_img()

        calender_image = ImageDraw(image)
        calender_image.text(
            xy=(18*self.scope, 18*self.scope),
            text="Calender",
            font=font_name,
            fill=self.FONT_COLOR
        )

        calender_image.rectangle(
            xy=((0, 0), (self.WIDTH, self.HEIGHT)),
            outline=self.OUTLINE_COLOR,
            width=5
        )

        point_x = 18 * self.scope
        point_y = 60 * self.scope
        for i in range(29):
            for j in range(7):
                dump = grass[random.randint(0, 4)]
                mask = self._round_img(dump)
                image.paste(im=dump, box=(point_x, point_y), mask=mask)
                point_y += 12 * self.scope + 4 * self.scope

            point_x += 12 * self.scope + 4 * self.scope
            point_y = 60 * self.scope

        return image


if __name__ == "__main__":
    user_profile = DrawProfile()
    img = user_profile.user_calender()
    img2 = user_profile.user_profile()
    img.show()
    img2.show()

    img.save(os.path.join(directory, "assets", "user_calender.png"))
    img2.save(os.path.join(directory, "assets", "user_profile.png"))

