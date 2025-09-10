from shutil import get_terminal_size
from time import time


def ft_tqdm(lst: range) -> None:
    meta_width = 31
    terminal_width = get_terminal_size()[0]
    bar_width = terminal_width - meta_width - len(f"{len(lst)}") * 2

    start_time = round(time(), 0)

    progress_ratio = lambda x: x / len(lst)

    for i, item in enumerate(lst, start = 1):
        elapsed_time = time() - start_time
        speed = i / elapsed_time if elapsed_time > 0 else 0

        actual_bar_width = bar_width - len(f"{speed:.0f}")

        bar_percentage = f'{progress_ratio(i) * 100:>3.0f}%|'
        bar_progress = f'{'█' * int(actual_bar_width * progress_ratio(i)):<{actual_bar_width}}'
        bar_data = f'| {i}/{len(lst)} []'
        print(f"\r{bar_percentage}{bar_progress}{bar_data}", end="", flush=True)
        yield item
