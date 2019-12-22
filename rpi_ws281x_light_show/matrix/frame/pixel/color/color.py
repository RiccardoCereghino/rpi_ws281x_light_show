from neopixel import Color as NeoColor


class Color:
    def __init__(self, r=0, g=0, b=0, w=0):
        self.r = r
        self.g = g
        self.b = b
        self.w = w

    def convert(self):
        return NeoColor(self.r, self.g, self.b, self.w)

    def black(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.w = 0

    def red(self):
        self.r = 255
        self.g = 0
        self.b = 0
        self.w = 0

    def green(self):
        self.r = 0
        self.g = 255
        self.b = 0
        self.w = 0

    def blue(self):
        self.r = 0
        self.g = 0
        self.b = 255
        self.w = 0

    def white(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.w = 255
