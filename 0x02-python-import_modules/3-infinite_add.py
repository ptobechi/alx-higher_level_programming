#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    n = len(argv)
    if n == 1:
        print(0)
    else:
        result = 0
        for i in argv[1:]:
            result += int(i)
        print(result)
