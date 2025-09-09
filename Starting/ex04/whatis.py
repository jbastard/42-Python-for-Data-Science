import sys

try:
    assert len(sys.argv) == 2, "Usage: python whatis.py <int>"

    num = int(sys.argv[1])
    assert isinstance(num, int), "Argument must be an integer."

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except ValueError:
    print("Argument must be an integer.")
except AssertionError as error:
    print(error)
