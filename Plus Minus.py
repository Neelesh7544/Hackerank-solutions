#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    p=0
    m=0
    z=0
    for i in arr:
        if(i>0):
            p+=1
        elif(i==0):
            z+=1
        else:
            m+=1
    print(float(p/len(arr)))
    print(float(m/len(arr)))
    print(float(z/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
