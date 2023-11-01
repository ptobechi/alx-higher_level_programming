#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)

if num < 0:
    remainder = num % -10
else:
    remainder = num % 10

if remainder > 5:
    print(
        f"Last digit of {num:d} is {remainder} and is greater than 5"
        )
elif remainder < 6 and remainder != 0:
    print(
        f"Last digit of {num:d} is {remainder} and is less than 6 and not 0"
        )
elif remainder == 0:
    print(f"Last digit of {num:d} is {remainder} and is 0")
