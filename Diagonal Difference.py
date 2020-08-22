#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    lsum=0
    rsum=0
    length=len(arr)
    for i in range(length):
        lsum+=arr[i][i]
        rsum+= arr[i][(length-i-1)]
    return abs(lsum-rsum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
