#!/usr/bin/python3
output = ""
for fir_digit in range(10):
    for sec_digit in range(fir_digit + 1, 10):
        output += "{:02d}, ".format(fir_digit * 10 + sec_digit)

print(output[:-2])
