
import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
  count_apple = 0
  count_orange = 0
  for apple in apples:
    fall = a + apple
    if fall >= s and fall <= t:
      count_apple += 1
  print(count_apple)

  for orange in oranges:
    fall = b + orange
    if fall >= s and fall <= t:
      count_orange += 1
  print(count_orange)

if __name__ == '__main__':
  s = 7
  t = 11
  a = 5
  b = 15
  m = 3
  n = 2

  apples = [-2, 2, 1]

  oranges = [5, -6]

  countApplesAndOranges(s, t, a, b, apples, oranges)