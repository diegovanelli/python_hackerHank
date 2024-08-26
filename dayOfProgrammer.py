#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
  if (year >= 1700 and year <= 1917):
    if (year % 400 == 0):
      return "12.09." + str(year)
    else:
      return "13.09." + str(year)
  else:
    if (year % 4 == 0 and year % 100 != 0):
      return "12.09." + str(year)
    else:
      return "13.09." + str(year)

if __name__ == '__main__':
  year = 1800

  result = dayOfProgrammer(year)

  print(result)