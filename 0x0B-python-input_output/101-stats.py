#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics
"""
import sys
import signal


def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)


def print_metrics():
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")


def process_line(line):
    parts = line.split(" ")
    if len(parts) >= 9:
        status_code = parts[8]
        file_size = int(parts[9])

        file_sizes.append(file_size)

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1


try:
    file_sizes = []
    status_code_counts = {}

    signal.signal(signal.SIGINT, signal_handler)

    for line_number, line in enumerate(sys.stdin, start=1):
        process_line(line)

        if line_number % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
