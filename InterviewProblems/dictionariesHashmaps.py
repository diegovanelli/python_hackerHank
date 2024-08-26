#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
# def freqQuery(queries):
#     result = {}
#     retorno = []
#     for query in queries:
#         if query[0] == 1:
#             data, count = query[1], result.get(query[1], 0)
#             result[data] = count + 1
#         elif query[0] == 2:
#             data, count = query[1], result.get(query[1], 0)
#             if count > 0:
#                 count = count - 1
#                 result[data] = count
#             if result.get(data) and count == 0:
#                 result.pop(data)
#         elif query[0] == 3:
#             count = query[1]
#             exists = any(value == count for value in result.values())
#             retorno.append('1' if exists else '0')
#     return retorno

from collections import defaultdict

def freqQuery(queries):
    data_count = defaultdict(int)
    freq_count = defaultdict(int)
    result = []
  
    for query, value in queries:
        if query == 1:
            freq_count[data_count[value]] -= 1
            data_count[value] += 1
            freq_count[data_count[value]] += 1
        elif query == 2:
            if data_count[value] > 0:
                freq_count[data_count[value]] -= 1
                data_count[value] -= 1
                freq_count[data_count[value]] += 1
        elif query == 3:
            result.append(1 if freq_count[value] > 0 else 0)
    
    return result


if __name__ == '__main__':

    queries = [(1,1), (2,2), (3,2), (1,1), (1,1), (2,1), (3,2)]

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
