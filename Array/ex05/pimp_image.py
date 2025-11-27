from numpy import array
import matplotlib.pyplot as plt


def show_img(arr):
    h, w = arr.shape[:2]
    dpi = plt.rcParams.get('figure.dpi', 100)
    figsize = (w / dpi, h / dpi)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(arr.astype('uint8'))
    ax.set_axis_off()
    plt.show()


def ft_invert(array_img) -> array:
    """
    Invert RGB channels in-place, show the image, and return [array].
    """
    h, w, c = array_img.shape
    imgcpy = array_img.copy()
    for i in range(h):
        for j in range(w):
            imgcpy[i, j, 0] = 255 - imgcpy[i, j, 0]
            imgcpy[i, j, 1] = 255 - imgcpy[i, j, 1]
            imgcpy[i, j, 2] = 255 - imgcpy[i, j, 2]
    show_img(imgcpy)
    return [imgcpy]


def ft_red(array_img) -> array:
    """
    Keep red channel, zero green and blue, show image, and return [array].
    """
    h, w, c = array_img.shape
    imgcpy = array_img.copy()
    for i in range(h):
        for j in range(w):
            imgcpy[i, j, 1] = 0
            imgcpy[i, j, 2] = 0

    show_img(imgcpy)
    return [imgcpy]


def ft_green(array_img) -> array:
    """
    Keep green channel, zero red and blue, show image, and return [array].
    """
    h, w, c = array_img.shape
    imgcpy = array_img.copy()
    for i in range(h):
        for j in range(w):
            imgcpy[i, j, 0] = 0
            imgcpy[i, j, 2] = 0
    show_img(imgcpy)
    return [imgcpy]


def ft_blue(array_img) -> array:
    """
    Keep blue channel, zero red and green, show image, and return [array].
    """
    h, w, c = array_img.shape
    imgcpy = array_img.copy()
    for i in range(h):
        for j in range(w):
            imgcpy[i, j, 0] = 0
            imgcpy[i, j, 1] = 0
    show_img(imgcpy)
    return [imgcpy]


def ft_grey(array_img):
    """
    Convert to greyscale by averaging channels, show image, and return array.
    """
    h, w, c = array_img.shape
    imgcpy = array_img.copy()
    for i in range(h):
        for j in range(w):
            grey = (int(imgcpy[i, j, 0])
                    + int(imgcpy[i, j, 1])
                    + int(imgcpy[i, j, 2])) / 3
            imgcpy[i, j, 0] = grey
            imgcpy[i, j, 1] = grey
            imgcpy[i, j, 2] = grey
    show_img(imgcpy)
    return [imgcpy]
