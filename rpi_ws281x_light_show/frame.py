from color import Color
from pixel import Pixel


class Frame:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.pixel_count = rows * cols
        self.pixels = [Pixel(x, y) for y in range(cols) for x in range(rows)]

    def get_position(self, x, y):
        return y * self.rows + x

    def update_pixel(self, x, y, color: Color = Color()):
        self.pixels[self.get_position(x, y)].color.r = color.r
        self.pixels[self.get_position(x, y)].color.g = color.g
        self.pixels[self.get_position(x, y)].color.b = color.b
        self.pixels[self.get_position(x, y)].color.w = color.w

    def fill(self):
        for y in range(self.rows - 1):
            for x in range(self.cols - 1):
                yield x, y, self.pixels[self.get_position(x, y)]

    def canvas(self):
        for y in range(self.rows - 1):
            for x in range(self.cols - 1):
                yield self.get_position(x, y), self.pixels[self.get_position(x, y)].color.convert()

    def print(self):
        for x in range(self.rows - 1):
            row = []
            for y in range(self.cols - 1):
                row.append(self.pixels[self.get_position(x, y)].color.convert())
            print(row)
        print()
