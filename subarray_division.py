#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
  # Write your code here
  count = 0
  for i in range(len(s)):
    if sum(s[i:i+m]) == d:
      count += 1
  return count

if __name__ == '__main__':
    s = [1, 2, 1, 3, 2]

    d = 3 # soma dos quadrados

    m = 2 # quantidade de quadrados

    result = birthday(s, d, m)

    print(result)
