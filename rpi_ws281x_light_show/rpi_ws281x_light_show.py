#!/usr/bin/env python3
import time

from color import Color
from matrix import Matrix

m = Matrix()

try:
    while True:
        m.cleanup()
        m.render()
        m.scrolling_text(Color(0, 127, 0), 50, "Cookie is not a cookie and is not a bad dog")

except KeyboardInterrupt:
    m.color_wipe()
    m.render()
    time.sleep(.05)
