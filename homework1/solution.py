from itertools import chain
from collections import defaultdict
from collections import Counter


def rotate_left(image):
    iteration = range(len(image[0])-1, -1, -1)
    return [[row[column] for row in image] for column in iteration]


def rotate_right(image):
    iteration = range(len(image[0]))
    return [[row[column] for row in image[::-1]] for column in iteration]


def invert(image):
    return [[(255-r, 255-g, 255-b) for r, g, b in row] for row in image]


def lighten_(pixel, alpha):
    return tuple(map(lambda x: int(x + alpha*(255 - x)), pixel))


def lighten(image, alpha):
    return [[lighten_(pixel, alpha) for pixel in row] for row in image]


def darken_(pixel, alpha):
    return tuple(map(lambda x: int(x - alpha*x), pixel))


def darken(image, alpha):
    return [[darken_(pixel, alpha) for pixel in row] for row in image]


def create_histogram(image):
    colours = ('red', 'green', 'blue')
    pixels = list(chain.from_iterable(image))
    by_colour = [[pixel[i] for pixel in pixels] for i in range(3)]
    return {colour: Counter(by_colour[i]) for i, colour in enumerate(colours)}
