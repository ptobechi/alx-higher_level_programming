#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    num = len(argv)
    if num == 1:
        print(f"{num-1:d} arguments.")
    else:
        print(f"{num-1:d} argument:" if num == 2 else f"{num-1:d} arguments:")
        for i in range(1, num):
            print(f"{i:d}: {argv[i]:s}")
