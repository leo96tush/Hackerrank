#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
scores = list(map(int,input().split()))
minimum = scores[0]
maximum = scores[0]
count_maximum = 0
count_minimum = 0
for i in range(len(scores)):
    if(scores[i]>maximum):
        maximum = scores[i]
        count_maximum = count_maximum+1
    if(scores[i]<minimum):
        minimum = scores[i]
        count_minimum = count_minimum+1
print(count_maximum,count_minimum)

