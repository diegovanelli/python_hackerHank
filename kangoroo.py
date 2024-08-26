#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):

  firstKangaroo = []
  secondKangaroo = []
  if (x1 < x2):
    firstKangaroo = [x1, v1]
    secondKangaroo = [x2, v2]
  else:
    firstKangaroo = [x2, v2]
    secondKangaroo = [x2, v2]
  
  while firstKangaroo[0] < secondKangaroo[0]:
    firstKangaroo[0] += firstKangaroo[1]
    secondKangaroo[0] += secondKangaroo[1]
  
  if firstKangaroo[0] == secondKangaroo[0]:
    return 'YES'
  else:
    return 'NO'

if __name__ == '__main__':

    x1 = 43

    v1 = 2

    x2 = 70

    v2 = 2

    result = kangaroo(x1, v1, x2, v2)
    print(result)