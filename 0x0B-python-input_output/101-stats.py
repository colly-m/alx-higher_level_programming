#!/usr/bin/python3
"""Function to read from stdin and computes metrics after every 10 lines"""


def print_stat(size, stat_codes):
    """Prints all gotten metrics"""
    print("File size: {}".format(size))
    for key in sorted(stat_codes):
        print("{}:{}". format(key, stat_codes[key]))

    if __name__ == "__main__":
        import sys

        size = 0
        stat_codes = {}
        v_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
        count = 0

        try:
            for line in sys.stdin:
                if count == 10:

                    print_stat(size, stat_codes)
                    count = 1
                else:
                    count += 1

                    line = line.split()
                try:
                    size += int(line[-1])
                except (IndexError, ValueError):
                    pass
                try:
                    if line[-2] in v_codes:
                        if stat_codes(line[-2], -1) == -1:
                            stat_codes[line]-2]] = 1
                        else:
                            stat_codes[line[-2]] += 1

                except IndexError:
                    pass

            print_stat(size, stat_codes)
            except KeyboardInterapt:
                print_stat(size, stat_codes)
                raise
