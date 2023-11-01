#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    l_digit = num % -10
else:
    l_digit = num % 10

if l_digit > 5:
    print(f"Last digit of {num:d} is {l_digit} and is greater than 5")
elif l_digit < 6 and l_digit != 0:
    print(f"Last digit of {num:d} is {l_digit} and is less than 6 and not 0")
elif l_digit == 0:
    print(f"Last digit of {num:d} is {l_digit} and is 0")
