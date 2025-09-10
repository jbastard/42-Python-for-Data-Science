from sys import argv
from ft_filter import ft_filter


def main():
    """Filter strings from command line input based on length.
    Usage: python3 filterstring.py <string> <int>
    Returns a list of words from the input string that ar
    longer than the specified length."""

    try:
        if (len(argv) != 3
                or not isinstance(argv[1], str)
                or not argv[2].isdigit()):
            raise AssertionError("python3 filterstring.py <string> <int>")
        N = int(argv[2])
        base_list = argv[1].split()
        print(list(ft_filter(lambda s: len(s) > N, base_list)))
    except Exception as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
