from .color.color import Color


class Pixel:
    def __init__(self, x, y, color: Color = Color()):
        self.x = x
        self.y = y
        self.color = color
