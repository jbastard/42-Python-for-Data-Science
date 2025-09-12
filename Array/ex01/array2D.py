def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D list (family) from start to end index
    and returns the sliced list.
    
    Args:
        family (list): 2D list to slice
        start (int): Starting index for slicing
        end (int): Ending index for slicing
    
    Returns:
        list: Sliced 2D list from start to end index
        
    Raises:
        TypeError: If input types are incorrect
        AssertionError: If family is not a square matrix
    """
    try:
        if (not isinstance(start, int)
                or not isinstance(end, int)
                or not isinstance(family, list)):
            raise TypeError("slice_me(family <list>, start <int>, end <int>)")

        if any(len(f) is not len(family[0]) for f in family):
            raise AssertionError("Family need to be a square.")

        print(f"My shape is ({len(family)}, {len(family[0])})")
        new_fam = family[start:end]
        print(f"My new shape is ({len(new_fam)}, {len(new_fam[0])})")
        return new_fam

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
