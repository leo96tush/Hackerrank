#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    length = len(s)
    number_of_sos = length//3
    count = 0
    required_message = ['S','O','S']*number_of_sos
    received_message = list(s)
    for i in range(len(s)):
        if(required_message[i]!=received_message[i]):
            count = count+1
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
