#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    num = len(argv)
    if num == 1:
        print(f"{n-1:d} arguments.")
    else:
        print(f"{n-1:d} argument:" if num == 2 else f"{n-1:d} arguments:")
        for i inum range(1, n):
            print(f"{i:d}: {argv[i]:s}")
