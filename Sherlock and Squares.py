#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    count = 0
    x = math.sqrt(a)
    y = math.sqrt(b)
    if(x==int(x)):
        m = x
        m = int(m)
    else:
        m = int(x)+1
    if(y==int(y)):
        n = y
        n = int(n)        
    else:
        n = int(y)
    
    for i in range(m,n+1):
        count = count+1
    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
