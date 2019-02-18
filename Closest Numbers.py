#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
n = int(input())
arr = list(map(int,input().split()))
sorted_arr = sorted(arr)[::-1]
minimum = 1000000
final_list = list()
for i in range(len(sorted_arr)-1):
    if(abs(sorted_arr[i+1]-sorted_arr[i])<minimum):
        minimum = abs(sorted_arr[i+1]-sorted_arr[i])
for i in range(len(sorted_arr)-1):
    if(abs(sorted_arr[i+1]-sorted_arr[i])==minimum):
        final_list.append(sorted_arr[i])
        final_list.append(sorted_arr[i+1])
print(*final_list[::-1],sep=' ')
        
    
