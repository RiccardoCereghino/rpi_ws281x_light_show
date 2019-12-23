import time
from neopixel import Adafruit_NeoPixel
from color import Color
from frame import Frame
from text import Text


class Matrix:
    def __init__(self):
        # LED strip configuration:
        self.led_count = 512  # Number of LED pixels.
        self.led_pin = 18  # GPIO pin connected to the pixels (18 uses PWM!).
        self.led_freq_hz = 800000  # LED signal frequency in hertz (usually 800khz)
        self.led_dma = 10  # DMA channel to use for generating signal (try 10)
        self.led_brightness = 15  # Set to 0 for darkest and 255 for brightest
        self.led_invert = False  # True to invert the signal (when using NPN transistor level shift)
        self.led_channel = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

        self.matrix = Adafruit_NeoPixel(self.led_count, self.led_pin, self.led_freq_hz, self.led_dma, self.led_invert,
                                        self.led_brightness, self.led_channel)

        self.matrix.begin()
        self.frame = Frame(rows=16, cols=32)

    def color_wipe(self, color: Color = Color()):
        for x, y, pixel in self.frame.fill():
            pixel.color = color

    def display_text(self, color: Color = Color(), row_1="", row_2=""):
        t_1 = Text(row_1)
        t_2 = Text(row_2)
        t = t_1.array + t_2.array

        for i in range(self.frame.cols()):
            for x, y, pixel in self.frame.fill():
                if t[x][y]:
                    pixel.color = color

    def scrolling_text(self, color: Color = Color(), repetitions=1, row_1="", row_2=""):
        t_1 = Text(row_1)
        t_2 = Text(row_2)
        t = t_1.array + t_2.array

        for rep in range(repetitions):
            for i in range(len(t)):
                for x, y, pixel in self.frame.fill():
                    if t[x][y]:
                        pixel.color = color
                self.render()
                time.sleep(.5)
                self.cleanup()
                temp = t.pop(0)
                t.append(temp)

    def render(self):
        for position, color in self.frame.canvas():
            self.matrix.setPixelColor(position, color)
        self.matrix.show()

    def cleanup(self):
        self.frame.fill()
