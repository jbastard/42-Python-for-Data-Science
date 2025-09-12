

def give_bmi(height: list[int | float], weight: list[int | float]):
    try:
        if len(height) is not len(weight):
            raise AssertionError("Height and weight lists "
                                 "must have the same length")

        if any(not isinstance(a, list) for a in zip(height, weight)):
            raise TypeError("Both height and weight "
                            "parameters need to be lists")

        if any(not isinstance(h, (int, float)) or not
                isinstance(w, (int, float)) for h, w in zip(height, weight)):
            raise AssertionError("List members "
                                 "needs to be integers or floats")

        return [w / (h * h) for h, w in zip(height, weight)]
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if any(not isinstance(b, (int, float)) for b in bmi):
            raise AssertionError("List members "
                                 "needs to be integers or floats")

        return [b > limit for b in bmi]
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
