#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def getTotalX(a, b):
  temp = []

  for i in range(1, brr[0]+1):
    all_zero = True
    for j in arr:
      if (i % j != 0):
        all_zero = False
    if (all_zero):
      temp.append(i)

  count = 0
  for i in temp:
    all_zero = True
    for j in brr:
      if (j % i != 0):
        all_zero = False
    if (all_zero):
      count += 1
  return count

if __name__ == '__main__':

  arr = [2, 4]
  brr = [16, 32, 96]
  total = getTotalX(arr, brr)
  
  print(count)
