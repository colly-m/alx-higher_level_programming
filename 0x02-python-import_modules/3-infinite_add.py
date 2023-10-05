#!/usr/bin/python3
import sys

if __name__ == "__main__":

    result = 0
    for a in range(len(sys.argv) - 1):
        result += int(sys.argv[a + 1])
    print("{}".format(result))
