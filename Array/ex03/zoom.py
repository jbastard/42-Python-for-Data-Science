from PIL import Image, UnidentifiedImageError
from load_image import ft_load


def zoom(arr_img, x, y):
    if arr_img is None:
        raise UnidentifiedImageError("Unable to load {animal.jpeg}")

    h, w, _ = arr_img.shape
    x1, x2 = x[0], x[1]
    y1, y2 = y[0], y[1]

    print(f"New shape after slicing: {arr_img[y1:y2, x1:x2].shape}")

    return arr_img[y1:y2, x1:x2]


def main():
    arr_img = ft_load("animal.jpeg")
    if arr_img is None:
        raise UnidentifiedImageError("Unable to load {animal.jpeg}")
    print(arr_img[:2])
    zoom_img = zoom(arr_img, (500, 800), (150, 450))
    print(zoom_img[:2])

    Image.fromarray(zoom_img).show()


if __name__ == "__main__":
    main()
