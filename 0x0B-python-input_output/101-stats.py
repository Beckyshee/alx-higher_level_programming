#!/usr/bin/python3
"""Reads from stdin and computes metrics.

After every ten lines or the input of a keyboard interrupt (^C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")


if __name__ == "__main__":
    from sys import stdin

    size, count = 0, 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
