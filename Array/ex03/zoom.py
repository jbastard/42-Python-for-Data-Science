from PIL import Image, UnidentifiedImageError
import numpy as np
from load_image import ft_load


def main():
    arr_img = ft_load("animal.jpeg")
    if arr_img is None:
        raise UnidentifiedImageError("Unable to load {animal.jpeg}")

    h, w, _ = arr_img.shape
    x1, x2 = 0, 50
    y1, y2 = 10, 60

    zoom = Image.fromarray(arr_img[x1:x2, y1:y2])
    zoom.show()

if __name__ == "__main__":
    main()
