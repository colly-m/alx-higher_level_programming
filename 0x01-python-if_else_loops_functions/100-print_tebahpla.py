#!/usr/bin/python3
for value in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:c}".format(value, value - 33), end="")
