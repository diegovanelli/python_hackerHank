
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

  # Complete the breakingRecords function in the editor below.

  # breakingRecords has the following parameter(s):

  # int scores[n]: points scored per game

  # Returns

  # int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
def breakingRecords(scores):
    high = low = scores[0]
    high_count = low_count = 0
    for score in scores[1]:
        if score > high:
            high = score
            high_count += 1
        elif score < low:
            low = score
            low_count += 1
    return [high_count, low_count]

if __name__ == '__main__':
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

    result = breakingRecords(scores)
    print(result)
  


if __name__ == '__main__':
  scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

  result = breakingRecords(scores)