#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


print("pangram" if len(Counter(input().lower())) == 27 else "not pangram")

