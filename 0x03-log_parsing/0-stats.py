#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """

import sys


def print_statistics(status_counts, total_size):
    """ Prints file size and status code counts """
    print("File size: {:d}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] != 0:
            print("{}: {:d}".format(status_code, status_counts[status_code]))


status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        if line_count % 10 == 0:
            print_statistics(status_counts, total_size)

        try:
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            total_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1

        except IndexError:
            continue
        except ValueError:
            continue

    print_statistics(status_counts, total_size)

except KeyboardInterrupt:
    print_statistics(status_counts, total_size)
    raise
