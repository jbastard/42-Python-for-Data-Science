
def odd_or_even(i: int):
    return i % 2 == 0


def ft_filter(function: callable, iterable: list):
    """Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None
    return the items that are true."""

    if function is None:
        new_list = [item for item in iterable if item]
    else:
        new_list = [item for item in iterable if function(item)]
