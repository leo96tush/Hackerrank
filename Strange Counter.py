#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    k = 4
    arr = list()
    arr.append(k)
    if(t==4):
        return(6)
    else:
        while(t>k):
            k = (2*k+2)
            arr.append(k)
        return(k-t)


if __name__ == '__main__':

    t = int(input())

    result = strangeCounter(t)

    print(result)
