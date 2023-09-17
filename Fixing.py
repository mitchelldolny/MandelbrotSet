import PIL

from PIL import Image, ImageDraw
import cmath
import math

xneg = -2
xpos = 1
yneg = -1.5
ypos = 1.5
maxiter = 800
h = 800
w = 800


def createIter(height, width):
    r = 0.533
    g = 0.137
    b = 0.882
    nextvalue = complex(0, 0)
    for j in range(maxiter + 5):
        startingVal = complex(currentPixelX, currentPixelY)
        nextvalue = nextvalue ** 2 + startingVal
        if nextvalue.real > 1 or nextvalue.real < -2:
            r += math.sqrt(j / maxiter)
            g += math.sqrt(j / maxiter)
            b += math.sqrt(j / maxiter)
            colour = (round(r % 1.0 * 255), round(g % 1.0 * 255), round(b % 1.0 * 255))
            return colour
        elif j >= maxiter:
            colour = (0, 0, 0)
            return colour


img = Image.new("RGB", (h, w), "white")
draw = ImageDraw.Draw(img)

# Creating a 2D array with 3 rows and 4 columns filled with zeros

matrix = [[[] for _ in range(w)] for _ in range(h)]

"""6
To make this zoom make a picture that reduces the picture frames down by a small amount and adjust the xneg and xpos accordingly 
this will slowly create a gif that will zoom in a certain location

pick two points one x and one y and then slowly reduce the other remaining sides in order for the picture to reduce in size

"""

"""
Go by each pixel along the x axis 
For each y point iterate 100 times
if still under 1 then print black
else print red

"""

for i in range(w):
    currentPixelX = xneg + i / w * 3
    for x in range(h):
        currentPixelY = yneg + x / h * 3
        col = createIter(currentPixelX, currentPixelY)
        draw.point((i, x), col)

img.save("mandelbrot.png", "png")
