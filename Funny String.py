#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    string_list = list(s)
    string_list_reverse = string_list[::-1]
    string_list_array = list()
    string_list_array_reverse = list()
    for i in range(len(string_list)-1):
        string_list_array.append(abs(ord(string_list[i+1])-ord(string_list[i])))
        string_list_array_reverse.append(abs(ord(string_list_reverse[i+1])-ord(string_list_reverse[i])))

    if(string_list_array==string_list_array_reverse):
        return('Funny')
    else:
        return('Not Funny')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
