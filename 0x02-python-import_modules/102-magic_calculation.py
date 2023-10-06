#!/usr/bin/python3
def magic_calculation(a, b):
    def add(g, h):
        return (g + h)

    def sub(g, h):
        return (g - h)

    if a < b:
        c = add(a, b)
        for y in range(4, 6):
            c = add(c, y)
        return (c)
    else:
        return (sub(a, b))
