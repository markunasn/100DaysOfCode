from math import floor, log10
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def sigfig(x, precision):
    x = float(x)
    return round(x, -int(floor(log10(abs(x)))) + (precision - 1))


def plusMinus(arr):
    positive = 0
    zero = 0
    negative = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    if positive != 0:
        positive = sigfig(positive / len(arr), 6)
    if zero != 0:
        zero = sigfig(zero / len(arr), 6)
    if negative != 0:
        negative = sigfig(negative / len(arr), 6)

    print(format(positive, '.6f'))
    print(format(negative, '.6f'))
    print(format(zero, '.6f'))

test = [1, -2, -7, 9, 1, -8, -5]
plusMinus(test)