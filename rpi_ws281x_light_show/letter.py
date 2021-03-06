from __future__ import print_function
from PIL import ImageFont, Image, ImageDraw
import numpy as np


class Letter:
    def __init__(self, char, font, fontsize=10):
        self.char = char
        self.font = font
        self.fontsize = fontsize
        self.array = []
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

    def fill_array(self, bool_list):
        offset = 8 - len(bool_list)
        for i in range(offset):
            if len(self.array) == 8:
                self.array[i] += [False] * len(bool_list[0])
            else:
                self.array.append([False] * len(bool_list[0]))

        for i in range(len(bool_list)):
            j = i + offset
            if len(self.array) == 8:
                self.array[j] += bool_list[i]
            else:
                self.array.append(bool_list[i])

    def render(self):
        for c in self.char:
            ttf_character = self.char_to_pixels(c)

            # Converts ttf_character to workable list
            bool_list = np.where(ttf_character, True, False)
            bool_list = bool_list.tolist()

            self.fill_array(bool_list)

