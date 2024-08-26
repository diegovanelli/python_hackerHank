#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_values = -9999
    for linha in range(4):
        linhaAcesso = linha
        colunaAcesso = 0
        for colunaAcesso in range(4):
            hourglasses = []
            for linha_final in range(linhaAcesso, linha + 3):
                arr_t = arr[linha_final][colunaAcesso:colunaAcesso+3]
                hourglasses.append(arr_t)
                linha_final += 1
            colunaAcesso += 1
            value_actual = 0
            for x in range(len(hourglasses)):
                if x == 1:
                    value_actual += hourglasses[x][1]
                else:
                    for y in range(3):
                        value_actual += hourglasses[x][y]
            if (value_actual > max_values):
                max_values = value_actual
            
        linha += 1
    return max_values
    

if __name__ == '__main__':
    # input = ["1 1 1 0 0 0",
    #         "0 1 0 0 0 0",
    #         "1 1 1 0 0 0",
    #         "0 0 2 4 4 0",
    #         "0 0 0 2 0 0",
    #         "0 0 1 2 4 0"]
    input = ["-9 -9 -9 1 1 1",
            "0 -9 0 4 3 2",
            "-9 -9 -9 1 2 3",
            "0 0 8 6 6 0",
            "0 0 0 -2 0 0",
            "0 0 1 2 4 0"]

    arr = []

    for _ in range(6):
        
        arr.append(list(map(int, input[_].rstrip().split())))

    result = hourglassSum(arr)
    
    print(result)

    
