def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Compute body mass index (BMI) values for corresponding sequences of heights
    and weights.

    Parameters
    ----------
    height : list[int | float]
      Sequence of heights (in metres). Each element must be an int or float.
    weight : list[int | float]
      Sequence of weights (in kilograms). Each element must be an int or float.

    Returns
    -------
    list[float]
      A list of BMI values computed element-wise as
      weight / (height ** 2).
      The returned list has the same length as the input sequences when
      inputs are valid.

    Raises
    ------
    ValueError
      If the height and weight lists do not have the same length.
    TypeError
      If the provided height or weight parameters are not sequences (list or
      tuple), or if any list member is not an int or float.

    Notes
    -----
    - Heights are expected in metres and weights in kilograms.
    - BMI is computed as weight / (height ** 2) for each corresponding pair.
    - The implementation catches exceptions, prints the exception type and
      message, and returns None on error; callers should be prepared to handle
      that.
    """
    try:
        if not isinstance(height, (list, tuple)) or not isinstance(
            weight, (list, tuple)
        ):
            raise TypeError("Both height and weight "
                            "parameters must be lists or tuples")

        if len(height) != len(weight):
            raise ValueError("Height and weight lists "
                             "must have the same length")

        if any(
            not isinstance(h, (int, float)) or not isinstance(w, (int, float))
            for h, w in zip(height, weight)
        ):
            raise TypeError("List members must "
                            "be integers or floats")

        return [w / (h * h) for h, w in zip(height, weight)]
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of booleans indicating which BMI values exceed a
    limit.
    Args:
      bmi (list or tuple of int|float): Sequence of BMI values to test.
      limit (int|float): Numeric threshold. Must be greater than zero.
    Returns:
      list[bool]: A list where each element is True if the corresponding
        BMI value is strictly greater than limit, otherwise False.
    Raises:
      TypeError: If `bmi` is not a list or tuple, if any member of `bmi`
        is not an int or float, or if `limit` is not numeric.
      ValueError: If `limit` is less than or equal to zero.
    Examples:
      >>> apply_limit([18.5, 25.0, 30.1], 25)
      [False, False, True]
    """
    try:
        if not isinstance(bmi, (list, tuple)):
            raise TypeError("BMI parameter needs to be a list or tuple")

        if any(not isinstance(b, (int, float)) for b in bmi):
            raise TypeError("List members must be integers or floats")

        if not isinstance(limit, (int, float)):
            raise TypeError("Limit needs to be an integer or float")

        if limit <= 0:
            raise ValueError("Limit must be greater than zero")

        return [b > limit for b in bmi]
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
