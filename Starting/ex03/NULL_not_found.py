no_arg = object()


def NULL_not_found(object: any = no_arg) -> int:
    if object is no_arg:
        return None
    if object is None:
        print("Nothing:", object, type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese:", object, type(object))
    elif isinstance(object, bool) and object is False:
        print("Fake:", object, type(object))
    elif isinstance(object, int) and object == 0:
        print("Zero:", object, type(object))
    elif isinstance(object, str) and object == "":
        print("Empty:", type(object))
    else:
        print("Type not found")
    return 1
