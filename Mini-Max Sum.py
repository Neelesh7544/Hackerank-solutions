#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #
    # Write your code here.
    #
    a=[]
    for i in arr:
        a.append(sum(arr)-i)
    print(min(a),max(a))
        
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
