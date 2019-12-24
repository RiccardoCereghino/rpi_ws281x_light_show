from __future__ import print_function
from PIL import ImageFont, Image, ImageDraw
import numpy as np


class Text:
    def __init__(self, text, font="dotty.ttf", fontsize=10):
        self.text = text
        self.font = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        self.fontsize = fontsize
        self.array = [[], [], [], [], [], [], [], []]
        self.render()

    def char_to_pixels(self, character):
        font = ImageFont.truetype(self.font, self.fontsize)
        w, h = font.getsize(character)
        h *= 2
        image = Image.new('L', (w, h), 1)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), character, font=font)
        arr = np.asarray(image)
        arr = np.where(arr, 0, 1)
        arr = arr[(arr != 0).any(axis=1)]
        return arr

    def render(self):
        for c in self.text:
            ttf_character = self.char_to_pixels(c)

            # Converts ttf_character to workable list
            bool_list = np.where(ttf_character, True, False)

            self.array[0] += [False] * len(bool_list[0])

            for i in range(len(bool_list)):
                self.array[i] += bool_list[i]