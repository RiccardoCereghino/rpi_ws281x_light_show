from neopixel import Color as NeoColor


class Color:
    def __init__(self, r=0, g=0, b=0, w=0):
        self.r = r
        self.g = g
        self.b = b
        self.w = w

    def convert(self):
        return NeoColor(self.r, self.g, self.b, self.w)

    @staticmethod
    def black():
        return Color(0, 0, 0, 0)

    @staticmethod
    def red():
        return Color(255, 0, 0, 0)

    @staticmethod
    def green():
        return Color(0, 255, 0, 0)

    @staticmethod
    def blue():
        return Color(0, 0, 255, 0)

    @staticmethod
    def white():
        return Color(0, 0, 0, 255)
