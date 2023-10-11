#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    totalWeight_sum = 0
    totalWeight = 0

    for score, weight in my_list:
        totalWeight_sum += score * weight
        totalWeight += weight

    if totalWeight == 0:
        return (0)

    weightAv = totalWeight_sum / totalWeight
    return (weightAv)
