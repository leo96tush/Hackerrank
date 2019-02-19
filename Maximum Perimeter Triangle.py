#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
n = int(input())
sticks = list(map(int,input().split()))
sorted_sticks = sorted(sticks)[::-1]
triangle = list()
for i in range(len(sticks)-2):
    if(sorted_sticks[i]<sorted_sticks[i+1]+sorted_sticks[i+2]):
        if(sorted_sticks[i+1]<sorted_sticks[i]+sorted_sticks[i+2]):
            if(sorted_sticks[i+2]<sorted_sticks[i]+sorted_sticks[i+1]):
                triangle.append(sorted_sticks[i])
                triangle.append(sorted_sticks[i+1])
                triangle.append(sorted_sticks[i+2])
                triangle = triangle[::-1]
                print(*triangle,sep=' ')
                break
else:
    print(-1)


