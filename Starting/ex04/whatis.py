from sys import argv

try:
    if not len(argv) == 2:
        raise AssertionError("Usage: python whatis.py <int>")

    if not argv[1].isdigit():
        raise AssertionError("Argument must be an integer.")
    num = int(argv[1])

    print("I'm Odd." if num % 2 else "I'm Even.")

except AssertionError as e:
    print(f"{type(e).__name__}: {e}")
