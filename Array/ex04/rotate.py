import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt

from load_image import ft_load
from zoom import zoom


def transpose(arr_img):
    """
    Transpose an image array by swapping height and width axes.

    Parameters
    ----------
    arr_img : numpy.ndarray
      Input image array with shape (H, W, C), where H is height,
      W is width and C is number of channels. The array's dtype is
      preserved in the result.

    Returns
    -------
    numpy.ndarray
      New image array with shape (W, H, C). For all valid indices i, j:
      output[j, i] == arr_img[i, j]. Channels and dtype are unchanged.

    Notes
    -----
    Performs an explicit element-wise copy; complexity is O(H*W*C) and
    additional memory of the same size is allocated. For a view-only
    transpose consider numpy.transpose.

    Raises
    ------
    AttributeError
      If arr_img has no 'shape' attribute.
    ValueError
      If arr_img.ndim < 2.
    """
    h, w, c = arr_img.shape
    new_image = np.empty((w, h, c), dtype=arr_img.dtype)
    for i in range(h):
        for j in range(w):
            new_image[j, i] = arr_img[i, j]
    return new_image


def main():
    try:
        img = ft_load("animal.jpeg")

        cropped = zoom(img, (400, 800), (150, 550))
        print(f"The shape of image is: {cropped.shape}\n{cropped[:1]}")

        transpo = transpose(cropped)
        print(f"New shape after Transpose: {transpo.shape}\n{transpo[:1]}")

        zoomed_image = Image.fromarray(np.asarray(transpo))
        grayscale_img = zoomed_image.convert("L")

        plt.imshow(grayscale_img, cmap='gray')
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
