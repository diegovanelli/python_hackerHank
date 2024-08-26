#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
  # Write your code here
  retorno = 0
  valor_maximo = 0
  for i in range(1, max(arr)+1):
    if (arr.count(i) > valor_maximo):
      valor_maximo = arr.count(i)
      retorno = i
  return retorno

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

    result = migratoryBirds(arr)

    print(result)
