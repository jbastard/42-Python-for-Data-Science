from shutil import get_terminal_size
from time import time


def format_time(time: float) -> str:
    """Convert time in seconds to formatted string in MM:SS format.

    Args:
        time (float): Time in seconds to be formatted.

    Returns:
        str: Formatted time string in "MM:SS" format, where MM is minutes
            and SS is seconds, both zero-padded to two digits.
    """

    return f"{int(time // 60):02d}:{int(time % 60):02d}"


def progress_ratio(x: int, y: int) -> float:
    """Calculate the ratio of progress by dividing x by y.

    Args:
        x (int): The current progress value (numerator)
        y (int): The total value (denominator)

    Returns:
        float: The ratio of x/y as a float between 0 and 1
    """

    return x / y


def ft_tqdm(lst: range) -> None:
    """Create a progress bar iterator similar to tqdm.

    This function wraps an iterable and yields each item while displaying
    a progress bar in the terminal. The progress bar shows completion
    percentage, elapsed time, estimated time remaining, and iteration speed.

    Args:
        lst (range): A range object to iterate over and display progress.

    Yields:
        Any: Items from the input range object one at a time.
    """

    meta_width = 31
    terminal_width = get_terminal_size()[0]
    bar_width = terminal_width - meta_width - len(f"{len(lst)}") * 2
    lenl = len(lst)
    start_time = round(time(), 0)

    for i, item in enumerate(lst, start=1):
        lap_time = time() - start_time
        speed = i / lap_time if lap_time > 0 else 1

        act_bar_width = bar_width - len(f"{speed:.0f}")
        bar_prog_data = int(act_bar_width * progress_ratio(i, lenl))
        lap_time = format_time(lap_time)
        left_time = format_time((lenl - i) / speed)
        bar_percent = f'{progress_ratio(i, lenl) * 100:>3.0f}%|'
        bar_progress = f'{'█' * bar_prog_data:<{act_bar_width}}'
        bar_data = f'| {i}/{lenl} [{lap_time}<{left_time}, {speed:0.2f}it/s]'

        print(f"\r{bar_percent}{bar_progress}{bar_data}", end="", flush=True)

        yield item
