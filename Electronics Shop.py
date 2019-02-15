#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards = sorted(keyboards)
    drives = sorted(drives)
    keyboards = keyboards[::-1]
    drives = drives[::-1]
    i = 0
    j = 0
    sum = list()
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            sum.append(keyboards[i]+drives[j])
    sum = sorted(sum)
    sum = sum[::-1]
    for i in range(len(sum)):
        if(sum[i]<=b):
            return(sum[i])
            break 
    return(-1)  

    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
