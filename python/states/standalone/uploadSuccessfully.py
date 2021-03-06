# Need neopixel

import time

from neopixel import *

class UploadSuccessfully(object):

	def __init__(self, stick):
		self.stick = stick

	def colorWipe(self, color, wait_ms=100):
		""" wipe color across display pixel a time """
		for i in range(self.stick.numPixels()):
			self.stick.setPixelColor(i, color)
			self.stick.show()
			time.sleep(0.05)

		for i in range(self.stick.numPixels()):
			self.stick.setPixelColor(i, Color(0, 0, 0))
			self.stick.show()
			time.sleep(0.05)

	def dimColor(self, color):
		""" Color is an 32-bit int that merges the values into one """
		return (((color & 0xff0000) / 3) & 0xff0000) + (((color & 0x00ff00) / 3) & 0x00ff00) + (
		((color & 0x0000ff) / 3) & 0x0000ff)

	def start(self):

		self.colorWipe(Color(255, 0, 0))



