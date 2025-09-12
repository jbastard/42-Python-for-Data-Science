from subprocess import Popen
from time import sleep
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


def install(log: bool):
    uninstall(log)
    build(log)
    cmd = "pip install ./dist/ft_package-0.0.1.tar.gz"
    if not log:
        cmd += " > /dev/null 2>&1"

    proc = Popen(cmd, shell=True)
    if log:
        proc.wait()
        return

    for i in tqdm(range(100), total=100, desc="Installing ft_package "):
        sleep(0.015)
        if i == 100:
            proc.wait()


def show(log: bool):
    install(log)
    try:
        cmd = "pip show -v ft_package"
        proc = Popen(cmd, shell=True)
        proc.wait()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def main():
    callable_func = {
        "build": build,
        "install": install,
        "uninstall": uninstall,
        "show": show,
        # "test": test,
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
