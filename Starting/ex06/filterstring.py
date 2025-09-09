from sys import argv
import ft_filter

def main():
    # Faire le prog dans le try catch
    try:
        if (len(argv) != 3
                or isinstance(argv[1], str)
                or isinstance(argv[2], int)):
            raise AssertionError("python3 filterstring.py <string> <int>")
    except Exception as error:
        print(f"{type(error).__name__}: {error}")

if __name__ == "__main__":
    main()