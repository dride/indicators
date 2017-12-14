# Need neopixel

import time
import os

from neopixel import *

class Error(object):
	def __init__(self, stick):
		self.stick = stick

	# Define functions which animate LEDs in various ways.
	def colorWipe(self, color, wait_ms=100):
		""" wipe color across display pixel a time """
		for i in range(self.stick.numPixels()):
			self.stick.setPixelColor(i, color)

		self.stick.show()
		time.sleep(0.5)



	def start(self):
		self.stick.begin()

		self.colorWipe(Color(0, 255, 0))



