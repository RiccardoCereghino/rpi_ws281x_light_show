from __future__ import print_function
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
import os


class Text:
    def __init__(self, text, font="dotty.ttf", fontsize=20):
        self.text = text
        self.font = "{}/assets/fonts/{}".format(os.getcwd(), font)
        self.fontsize = fontsize
        self.array = []

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

            for i in range(len(bool_list)):
                self.array.append(bool_list[i])
