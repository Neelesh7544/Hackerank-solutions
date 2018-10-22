#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i in range(0,len(grades)):
        if(grades[i] >= 38 and grades[i] % 5 >2):
            grades[i] = grades[i] + (5 - (grades[i] % 5))
    return grades        
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
grades= solve(grades)
for i in range(0,len(grades)):
    print(grades[i])


