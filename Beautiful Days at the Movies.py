#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for t in range(i,j+1):
        number = list(map(int,str(t)))
        number_reverse = number[::-1]
        p = abs(int("".join(map(str, number)))-int("".join(map(str, number_reverse))))
        if((p%k)==0):
            count=count+1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
