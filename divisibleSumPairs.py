#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
  count = 0
  for i in range(n):
    for j in range(i+1, n):
      if ((ar[i] + ar[j]) % k == 0):
        count += 1
  return count

if __name__ == '__main__':
  n = 6

  k = 3

  ar = [1, 3, 2, 6, 1, 2]

  result = divisibleSumPairs(n, k, ar)

  print(result)
