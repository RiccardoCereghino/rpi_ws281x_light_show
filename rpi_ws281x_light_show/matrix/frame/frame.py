from .pixel.pixel import Pixel, Color


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

    def fill(self, color: Color = Color()):
        for y in range(self.cols - 1):
            for x in range(self.rows - 1):
                self.update_pixel(x, y, color)

    def canvas(self):
        for y in range(self.cols):
            for x in range(self.rows):
                yield self.get_position(x, y), self.pixels[self.get_position(x, y)].color.convert()
