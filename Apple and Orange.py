#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
acount=0
ocount=0
for i in apple:
    i=a+i
    if (i>=s and i<=t):
        acount=acount+1
for i in orange:
    i=b+i
    if (i>=s and i<=t):
        ocount=ocount+1
print(acount)
print(ocount)
