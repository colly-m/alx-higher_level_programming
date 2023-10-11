#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    romDictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0

    for numeral in range(len(roman_string)):
        if numeral > 0 and romDictionary[roman_string[numeral]] > romDictionary[roman_string[numeral - 1]]:
            result += romDictionary[roman_string[numeral]] - 2 * \
                    romDictionary[roman_string[numeral - 1]]
        else:
            result += romDictionary[roman_string[numeral]]

    return (result)
