#!/usr/bin/env python

import colorsys
import time
from sys import exit

try:
    import numpy as np
except ImportError:
    exit('This script requires the numpy module\nInstall with: sudo pip install numpy')

import blinkt

blinkt.set_clear_on_exit()

def make_gaussian(fwhm):
    x = np.arange(0, blinkt.NUM_PIXELS, 1, float)
    y = x[:, np.newaxis]
    x0, y0 = 3.5, 3.5
    fwhm = fwhm
    return np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)

def animate(hue, times=1):
    y = 4

    s = 1.0
    for _ in range(times):
        for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
            fwhm = 5.0 / z
            gauss = make_gaussian(fwhm)
            start = time.time()
            for x in range(blinkt.NUM_PIXELS):
                h = hue
                v = gauss[x, y]
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r, g, b = [int(255.0 * i) for i in rgb]
                blinkt.set_pixel(x, r, g, b)

            blinkt.show()
            end = time.time()
            t = end - start

            if t < 0.04:
                time.sleep(0.04 - t)

if(__name__ == '__main__'):
    animate(0.9,2)
