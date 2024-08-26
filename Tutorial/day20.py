#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    swaps = []
    # Write your code here
    for i in range(n):
        numberOfSwaps = 0;
        for j in range(n):
            try:
                index_plus = j + 1
                if (n != index_plus and a[j] > a[index_plus]):
                    temp = a[j]
                    a[j] = a[index_plus]
                    a[index_plus] = temp
                    numberOfSwaps = numberOfSwaps+1
            except Exception:
                print(index_plus)
        swaps.append(numberOfSwaps)
        if (numberOfSwaps == 0):
            break
    print("Array is sorted in {} swaps.".format(sum(swaps)))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))