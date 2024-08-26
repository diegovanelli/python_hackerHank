#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
    # (0,1,3) e (0,2,3)
    # [1,2,4] e [1,2,4]
    
    # (0,1,2,3, 4, 5)
    # [1,3,9,9,27,81]
    # (0,1,2) e (0,1,3) e (1,2, 4) e (1,3, 4) e (2, 4, 5) e (3, 4, 5)
    # [1,3,9] e [1,3,9] e [3,9,27] e [3,9,27] e [9,27,81] e [9,27,81]
    
    # (0,1,2, 3,  4)
    # [1,5,5,25,125]
    # (0,1, 3) e (0,2, 3) e (1, 3,  4) e (2, 3,  4)
    # [1,5,25] e [1,5,25] e [5,25,125] e [5,25,125]
def countTriplets(arr, r):
    # Initialize the dictionaries
    r2 = {}
    r3 = {}
    count = 0

    # Loop through the arr[] list
    for i in arr:

        # i is the third value of the geometric progression triplet
        # If i exists in the r3 dictionary then get the value of i from r3
        # and add it to count variable
        if i in r3:
            count += r3[i]

        # i is the second value of the geometric progression triplet
        # If i exists in the r3 dictionary then add the value of i from r3
        # to the r3 dictionary incremented by the value of i//r if it exists in
        # the r2 dictionary or add it to r3 dictionary and initialize it as 1
        if i in r2:
            if i*r in r3:
                r3[i*r] += r2[i]
            else:
                r3[i*r] = r2[i]

        # Count the instances of the first elements of possible
        # geometric progression triplets
        if i*r in r2:
            r2[i*r] += 1
        else:
            r2[i*r] = 1

    return count
if __name__ == '__main__':
    r = 4

    arr = [1,4,16,64]

    ans = countTriplets(arr, r)

    print(ans)
