#!/bin/python3

import math
import os
import random
import re
import sys

for _ in range(int(input())):
    n = int(input())
    p = list()
    num = 0
    for i in range(32):
        k = n%2
        if(k==1):
            p.append(0)
        else:
            p.append(1)
        n = n//2
    for i in range(32):
        num = num + (2**i)*p[i]
    print(num)
