import numpy as np
import PIL.Image as Image
from load_image import ft_load


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def zoom(arr_img, x, y):
    return arr_img[y[0]:y[1], x[0]:x[1]]


def transpose(arr_img):
    h, w, c = arr_img.shape
    new_image = np.empty((w, h, c), dtype=arr_img.dtype)
    for i in range(h):
        for j in range(w):
            new_image[j, i] = arr_img[i, j]
    return new_image

def main():
    img = ft_load("animal.jpeg")

    cropped = zoom(img, (400, 800), (150, 550))
    print(f"The shape of image is: {cropped.shape}\n{cropped[:1]}")

    transposed = transpose(cropped)
    print(f"New shape after Transpose: {transposed.shape}\n{transposed[:1]}")

    Image.fromarray(transposed).show()

    return

if __name__ == "__main__":
    main()
