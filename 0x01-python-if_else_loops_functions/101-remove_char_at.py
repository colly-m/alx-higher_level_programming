#!/usr/bin/python3
def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        return (input_str)

    result = ""
    for s in range(len(input_str)):
        if s != n:
            result += input_str[s]
    return (result)
