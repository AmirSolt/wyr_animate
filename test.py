from PIL import Image, ImageDraw

# Create first image
img1 = Image.new(mode="RGB", size=(500,500), color =(73, 109, 137))
draw = ImageDraw.Draw(img1)
draw.rectangle([(100, 100), (400, 400)], fill ="#FFFF33")
img1.save("img1.png")

# Create second image
img2 = Image.new(mode="RGB", size=(500,500), color =(0,90,50))
draw = ImageDraw.Draw(img2)
draw.ellipse([(100, 100), (400, 400)], fill ="#FF5733")
img2.save("img2.png")

from moviepy.editor import *


ic_1 = ImageClip('img1.png').set_duration(2)
ic_2 = ImageClip('img2.png').set_duration(1)

video = concatenate([ic_1, ic_2], method="compose")
video.write_videofile('test.mp4', fps=24)