#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    minus=0
    plus=0
    zero=0
    for i in range(0,len(arr)):
        if(arr[i]>0):
            plus+=1
        elif(arr[i]<0):
            minus+=1
        else:
            zero+=1
    print(round(plus/len(arr),5))
    print(round(minus/len(arr),5))
    print(round(zero/len(arr),5))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
