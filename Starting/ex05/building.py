from sys import argv


PUNCTUATION_CHARS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def str_describe(str):
    """
    Analyze and provide a detailed summary of a given string by counting the
    occurrences of various character types. This includes upper-case letters,
    lower-case letters, punctuation marks, spaces, and numerical digits.

    :param str: The string to be analyzed.
    :type str: str
    :return: None
    """
    print(f"The text contains {len(str)} characters:")
    print(sum(1 for c in str if c.isupper()), "upper letters")
    print(sum(1 for c in str if c.islower()), "lower letters")
    print(sum(1 for c in str if c in PUNCTUATION_CHARS), "punctuation marks")
    print(sum(1 for c in str if c.isspace()), "spaces")
    print(sum(1 for c in str if c.isdigit()), "digits")


def main():
    """
    Main function that handles command-line arguments and string analysis.
    Expects exactly one command-line argument - the string to be analyzed.
    If an incorrect number of arguments is provided,
    displays a usage message and exits.

    Usage: python3 building.py <string>
    """

    try:
        if len(argv) > 2:
            raise AssertionError("Too much arguments, try with one or zero")
        if len(argv) == 1:
            str_describe(input("What is the text to count?\n") + "\n")
        else:
            str_describe(argv[1])
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
