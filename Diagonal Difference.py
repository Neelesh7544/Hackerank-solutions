#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    sum_d1=0
    sum_d2=0
    j=0
    for i in a:
        sum_d1+=i[j]
        j=j+1
    k=-1
    for i in a:
        sum_d2+=i[k]
        k=k-1
    return abs(sum_d1-sum_d2)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
