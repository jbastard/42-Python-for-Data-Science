from curses.ascii import islower, isupper, ispunct, isspace, isdigit
from sys import argv


def str_describe(str):
    """
    Analyze and provide a detailed summary of a given string by counting the
    occurrences of various character types. This includes upper-case letters,
    lower-case letters, punctuation marks, spaces, and numerical digits.

    :param str: The string to be analyzed.
    :type str: str
    :return: None
    """

    upper_chars = sum(1 for c in str if isupper(c))
    lower_chars = sum(1 for c in str if islower(c))
    punct_chars = sum(1 for c in str if ispunct(c))
    spaces = sum(1 for c in str if isspace(c))
    digits = sum(1 for c in str if isdigit(c))

    print(f"The text contains {len(str)} characters:")
    print(upper_chars, "upper letters")
    print(lower_chars, "lower letters")
    print(punct_chars, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


def main():
    """
    Main function that handles command-line arguments and string analysis.
    Expects exactly one command-line argument - the string to be analyzed.
    If an incorrect number of arguments is provided,
    displays a usage message and exits.

    Usage: python3 building.py <string>
    """

    try:
        assert len(argv) <= 2, "Too much arguments, try with one or zero"
        if len(argv) == 1:
            str_describe(input("What is the text to count?\n"))
        else:
            str_describe(argv[1])
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    except AssertionError as error:
        print(error)
        exit(1)


if __name__ == "__main__":
    main()
