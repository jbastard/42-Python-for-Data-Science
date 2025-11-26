from PIL import UnidentifiedImageError
import matplotlib.pyplot as plt
from load_image import ft_load


def _validate_range(start, stop, max_val, name):
    """Vérifie que start < stop et que les indices sont dans [0, max_val].
    Lève ValueError avec un message explicite si la vérification échoue.
    - name : 'x' ou 'y' pour formater le message d'erreur.
    """
    if not (start < stop):
        raise ValueError(f"{name} start must be < {name} stop (got {start} "
                         f">= {stop})")
    if start < 0 or stop < 0 or start > max_val or stop > max_val:
        raise ValueError(f"{name} indices out of bounds: must "
                         f"be between 0 and {max_val} (got {start}, {stop})")


def zoom(arr_img, x, y):
    """Return a rectangular sub-image by slicing a NumPy array.

    Parameters
    ----------
    arr_img : numpy.ndarray
      Image array with shape (h, w, c) or at least 2-D.
    x : tuple[int, int]
      Column range (x1, x2). Uses Python/NumPy slice semantics:
      start at x1 (inclusive) and stop at x2 (exclusive).
    y : tuple[int, int]
      Row range (y1, y2). Uses Python/NumPy slice semantics.

    Returns
    -------
    numpy.ndarray
      The slice arr_img[y1:y2, x1:x2]; typically a view (no copy).
      The returned array preserves a channel axis if present.

    Raises
    ------
    TypeError
      If x or y are not tuples or contain non-integer entries.
    ValueError
      If x or y do not have length 2 or indices are out of bounds.

    Notes
    -----
    This implementation enforces bounds checks: indices must be integers
    within [0, width] / [0, height] and start < stop.
    """
    if not (isinstance(x, tuple) and isinstance(y, tuple)):
        raise TypeError("x and y must be tuples")
    if not (len(x) == 2 and len(y) == 2):
        raise ValueError("x and y must be of length 2")
    if not all(isinstance(i, int) for i in x + y):
        raise TypeError("x and y must contain integers only")

    if arr_img.ndim < 2:
        raise ValueError("arr_img must be at least 2-D")
    h, w = arr_img.shape[:2]

    x1, x2 = x[0], x[1]
    y1, y2 = y[0], y[1]

    _validate_range(x1, x2, w, "x")
    _validate_range(y1, y2, h, "y")

    print(f"New shape after slicing: {arr_img[y1:y2, x1:x2].shape}")

    return arr_img[y1:y2, x1:x2]


def main():
    try:
        arr_img = ft_load("animal.jpeg")
        if arr_img is None:
            raise UnidentifiedImageError("Unable to load {animal.jpeg}")
        print(arr_img[:2])
        zoom_img = zoom(arr_img, (500, 1800), (150, 450))
        print(zoom_img[:2])

        plt.imshow(zoom_img)
        plt.title("Zoomed Image")
        plt.rcParams['toolbar'] = 'None'
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
