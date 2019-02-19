#!/bin/python3

import math
import os
import random
import re
import sys

for _ in range(int(input())):
    s = list(input())
    s_inverted = s[::-1]
    length_of_string = len(s)
    sum_value = 0
    for i in range(length_of_string):
        if(s[i]!=s_inverted[i]):
            sum_value = sum_value+abs(ord(s[i])-ord(s_inverted[i]))
    print(sum_value//2)
