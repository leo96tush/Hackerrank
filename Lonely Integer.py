#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
arr = list(map(int,input().split()))
p = max(arr)
count = [0]*(p+1)
for i in range(len(arr)):
    count[arr[i]]= count[arr[i]]+1

for i in range(len(count)):
    if(count[i]==1):
        print(i)
        break
