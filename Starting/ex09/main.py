from subprocess import Popen
from time import sleep
import os
from sys import argv
from tqdm import tqdm


def build(log: bool):
    cmd = "python3 -m build"
    if not log:
        cmd += " > /dev/null 2>&1"

    proc = Popen(cmd, shell=True)
    if log:
        proc.wait()
        return

    for i in tqdm(range(100), total=100, desc="Build "):
        sleep(0.015)
        if i == 100:
            proc.wait()


def uninstall(log: bool):
    cmd = "rm build dist ft_package.egg-info -rf; pip uninstall ft_package"
    proc = Popen(cmd, shell=True)
    proc.wait()


def main():
    callable_func = {
        "build": build,
        # "install": install,
        # "show": show,
        # "test": test,
        "uninstall": uninstall,
        # "full_install": full_install,
        # "full_run": full_run,
        # "re": re,
        # "re_test": re_test
    }
    try:
        verbose_mode = False
        if len(argv) < 2 or argv[1] not in callable_func:
            raise AssertionError("Usage: main.py <func> [-v, --verbose]")
        if len(argv) == 3 and argv[2] not in ["-v", "--verbose"]:
            raise AssertionError("Usage: main.py <func> [-v, --verbose]")
        if len(argv) == 3 or argv[1] == 'show':
            verbose_mode = True
        callable_func[argv[1]](verbose_mode)

    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main()
