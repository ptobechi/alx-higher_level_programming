#!/usr/bin/python3
for char in range(90, 64, -1):
    print(f"{chr(char)}", end="")
    char += 32 if char % 2 == 0 else 0
