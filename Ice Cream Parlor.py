#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
n_testcases = int(input())
array = list()
for _ in range(n_testcases):
    m = int(input())
    n = int(input())
    array = list()
    cost = list(map(int,input().split()))
    for i in range(len(cost)):
        for j in range(i+1,len(cost)):
            if(cost[i]+cost[j]==m and i!=j):
                array.append(i+1)
                array.append(j+1)
                break
    print(*array,sep=' ')
'''print(array)'''
