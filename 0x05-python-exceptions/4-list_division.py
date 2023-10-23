#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    outcome = []
    result = 0

    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]

        except TypeError:
            result = 0
            print("wrong type")

        except ZeroDivisionError:
            result = 0
            print("division by 0")

        except IndexError:
            result = 0
            print("Out of range")

        finally:
            pass
        outcome.append(result)

    return (outcome)
