#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hr=int(s[0:2])
    mm=s[3:5]
    ss=s[6:8]
    if s[8:10]=="PM":
        if(hr!=12):
            hr+=12
    else:
        if(hr == 12):
            hr="00"
    return str(hr).zfill(2) + ":" + mm + ":" + ss
        
            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
