from PIL import Image, ImageDraw
import math
import sys
import traceback

def drawHorizontalRedStripes(img):
	draw = ImageDraw.Draw(img)

	step = math.floor(img.height/10)
	lineWidth = max(math.floor(img.height * 0.03), 1)

	for i in range(0, img.height, step):
		startX = 0
		endX = img.width
		startY = endY = i
		draw.line((startX, startY, endX, endY), fill='red', width=lineWidth)

def alterImage(filename) -> None:
	with Image.open(filename) as img:
		try:
			drawHorizontalRedStripes(img)
		except Exception as ex:
			print("Couldn't alter image: {}".format(filename))
			traceback.print_exc()
		img.save(filename)