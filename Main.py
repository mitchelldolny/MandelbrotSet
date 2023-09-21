import PIL

from PIL import Image, ImageDraw
import cmath
import math

xneg = -2
xpos = 1
yneg = -1.5
ypos = 1.5
maxiter = 600
h = 800
w = 800
colours = [
    (44, 44, 84),
    (64, 64, 122),
    (34, 112, 147),
    (44, 44, 84),
    (52, 172, 224),
    (33, 140, 116),
    (179, 57, 57),
    (255, 82, 82),
    (255, 121, 63),
    (205, 97, 51),
    (204, 142, 53),
    (255, 177, 66)
]


def createIter(height, width):
    nextvalue = complex(0, 0)
    for j in range(maxiter + 5):
        startingVal = complex(currentPixelX, currentPixelY)
        nextvalue = nextvalue ** 2 + startingVal
        if nextvalue.real > 1 or nextvalue.real < -2:
            # r += math.sqrt(j / maxiter)
            # g += math.sqrt(j / maxiter)
            # b += math.sqrt(j / maxiter)
            # colour = (round(r % 1.0 * 255), round(g % 1.0 * 255), round(b % 1.0 * 255))
            return j, nextvalue
        elif j >= maxiter:
            # colour = (0, 0, 0)
            return maxiter, nextvalue


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


def linearInterpolateColor(value, ratio):
    index1 = min(len(colours) - 1, int(value))
    index2 = min(len(colours) - 1, int(value + 1))
    red = int(colours[index2][0] * ratio + colours[index1][0] * (1 - ratio))
    green = int(colours[index2][1] * ratio + colours[index1][1] * (1 - ratio))
    blue = int(colours[index2][2] * ratio + colours[index1][2] * (1 - ratio))
    tuple_returned = (red, green, blue)
    return tuple_returned


def ratio(c, iterations, max_iterations):
    if iterations < max_iterations:
        return 1 + iterations - math.log(math.log(c.real**2 + c.imag**2) / (2 * math.log(2))) / math.log(2  )
    return 0

for i in range(w):
    currentPixelX = xneg + i / w * 3
    #currentPixelX = i * (xpos - xneg) / (w - 1) + xneg
    for x in range(h):
        currentPixelY = yneg + x / h * 3
        #currentPixelY = x * (ypos - yneg) / (h - 1) + yneg
        col, complex_val = createIter(currentPixelX, currentPixelY)
        rat = ratio(complex_val, col, maxiter)
        colour = linearInterpolateColor(rat, rat % 1.0)
        draw.point((i, x), colour)

img.save("mandelbrot.png", "png")
