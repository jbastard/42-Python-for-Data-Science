from sys import argv


MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
}


def main():
    """
    Convert alphanumeric string to morse code.

    Takes a single command-line argument and converts it to morse code using
    MORSE_DICT. Only letters, numbers and spaces are allowed.

    Raises:
        AssertionError: If number of arguments is not 2 (script name + 1 arg)
        TypeError: If input has invalid characters
    """

    try:
        if len(argv) != 2:
            raise AssertionError("the arguments are bad")
        S = argv[1].upper()

        if not all(c in MORSE_DICT for c in S):
            raise AssertionError("the arguments are bad")
        print(*(MORSE_DICT[c] for c in S), end='')

    except Exception as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
