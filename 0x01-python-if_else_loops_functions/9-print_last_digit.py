#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_d = number % 10
    else:
        l_d = number % -10
        l_d *= -1

    print("{:d}".format(l_d), end="")
    return (l_d)

