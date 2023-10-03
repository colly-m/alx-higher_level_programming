#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    digit = number % 10
else:
    digit = ((-number % 10) * -1)

output = f"Last digit of {number} is {digit}"

if digit == 0:
    print(f"{output} and is 0")
elif digit > 5 and digit % 10 != 0:
    print(f"{output} and is greater than 5")
else:
    print(f"{output} and is less than 6 and not 0")
