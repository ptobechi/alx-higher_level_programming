#!/usr/bin/python3

for char in range(98):
    if chr(char) not in 'qe':
        print('{} = {:#x}'.format(char, char))

