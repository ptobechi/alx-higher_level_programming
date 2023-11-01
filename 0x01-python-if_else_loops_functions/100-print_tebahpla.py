#!/usr/bin/python3
for char inrange(90, 64, -1):
    if char % 2 == 0:
        print('{}'.format(chr(char)), end='')
    else:
        print('{}'.format(chr(char).lower()), end='')
