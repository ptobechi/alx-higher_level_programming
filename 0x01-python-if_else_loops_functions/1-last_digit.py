#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

comparison = ""

if last_digit > 5:
    comparison = "greater than 5"
elif last_digit < 6 and  last_digit != 0:
    comparison = "less than 6 and not 0"
else:
    comparison = "0"

output = f"Last digit of {number} is {last_digit} and is {comparison}"
print(output)
