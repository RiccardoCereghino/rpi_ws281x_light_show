from neopixel import Adafruit_NeoPixel
from rpi_ws281x_light_show.matrix.frame.pixel.color.color import Color
from rpi_ws281x_light_show.matrix.frame.frame import Frame


class Matrix:
    def __init__(self):
        # LED strip configuration:
        self.led_count = 512  # Number of LED pixels.
        self.led_pin = 18  # GPIO pin connected to the pixels (18 uses PWM!).
        self.led_freq_hz = 800000  # LED signal frequency in hertz (usually 800khz)
        self.led_dma = 10  # DMA channel to use for generating signal (try 10)
        self.led_brightness = 255  # Set to 0 for darkest and 255 for brightest
        self.led_invert = False  # True to invert the signal (when using NPN transistor level shift)
        self.led_channel = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

        self.matrix = Adafruit_NeoPixel(self.led_count, self.led_pin, self.led_freq_hz, self.led_dma, self.led_invert,
                                        self.led_brightness, self.led_channel)

        self.matrix.begin()
        self.frame = Frame(rows=16, cols=32)

    def fill_matrix(self, color: Color = Color()):
        self.frame.fill(color)

    def render(self):
        for position, color in self.frame.canvas():
            self.matrix.setPixelColor(position, color)
        self.matrix.show()

    def cleanup(self):
        self.frame.fill()
