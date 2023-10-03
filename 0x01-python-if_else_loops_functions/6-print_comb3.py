#!/usr/bin/python3
for fir_digit in range(10):
    for sec_digit in range(fir_digit + 1, 10):
        print("{}{}, ".format(fir_digit, sec_digit), end="")

print()
