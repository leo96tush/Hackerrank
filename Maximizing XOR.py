#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
l = int(input())
r = int(input())
maximum = -1000000
for i in range(l,r+1):
    for j in range(l,r+1):
        if((i^j)>=maximum):
            maximum = (i^j)

print(maximum)
