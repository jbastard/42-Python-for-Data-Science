from PIL import Image
import numpy as np
import os


def ft_load(path: str):
    """Load an image from a file path and convert it to a numpy array.

    Args:
        path (str): Path to the image file.

    Returns:
        numpy.ndarray: Array containing RGB values of the image.

    Raises:
        TypeError: If path is not a string.
        FileNotFoundError: If image file is not found.
    """
    try:
        if not isinstance(path, str):
            raise TypeError(f"Path need to be a string,"
                            f" got {type(path)} instead")
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Image not found: {path}")

        with Image.open(path) as f:
            img_format = f.format or "Unknow"
            rgb_img = f.convert("RGB")
            arr = np.array(rgb_img)

        print(f"Image format: {img_format}")
        print(f"The shape of image is: {arr.shape}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return arr
