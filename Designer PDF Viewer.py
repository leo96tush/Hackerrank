#!/bin/python3

import math
import os
import random
import re
import sys

string_values = list(map(int,input().split()))
string = input()
string = list(string)
length_of_string = len(string)
max_value = 0

for i in range(len(string)):
    if(string_values[ord(string[i])-97]>=max_value):
        max_value = string_values[ord(string[i])-97]
print(max_value*length_of_string)
