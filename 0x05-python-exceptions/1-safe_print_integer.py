#!/usr/bin/python3
def safe_print_integer(value):
    try:
        val = "{:d}".format(value)
        print(val)

        return (True)
    except (ValueError, TypeError):
        return (False)
