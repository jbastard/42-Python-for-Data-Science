from PIL import Image
from numpy import array


def ft_invert(array_img) -> array:
    h, w, c = array_img.shape
    for i in range(h):
        for j in range(w):
            array_img[i, j, 0] = 255 - array_img[i, j, 0]
            array_img[i, j, 1] = 255 - array_img[i, j, 1]
            array_img[i, j, 2] = 255 - array_img[i, j, 2]
    Image.fromarray(array_img).show()
    return [array_img]


def ft_red(array_img) -> array:
    h, w, c = array_img.shape
    for i in range(h):
        for j in range(w):
            array_img[i, j, 1] = 0
            array_img[i, j, 2] = 0
    Image.fromarray(array_img).show()
    return [array_img]


def ft_green(array_img) -> array:
    h, w, c = array_img.shape
    for i in range(h):
        for j in range(w):
            array_img[i, j, 0] = 0
            array_img[i, j, 2] = 0
    Image.fromarray(array_img).show()
    return [array_img]


def ft_blue(array_img) -> array:
    h, w, c = array_img.shape
    for i in range(h):
        for j in range(w):
            array_img[i, j, 0] = 0
            array_img[i, j, 1] = 0
    Image.fromarray(array_img).show()
    return [array_img]


def ft_grey(array_img):
    h, w, c = array_img.shape
    for i in range(h):
        for j in range(w):
            grey = (int(array_img[i, j, 0])
                    + int(array_img[i, j, 1])
                    + int(array_img[i, j, 2])) / 3
            array_img[i, j, 0] = grey
            array_img[i, j, 1] = grey
            array_img[i, j, 2] = grey
    Image.fromarray(array_img).show()
    return array_img
