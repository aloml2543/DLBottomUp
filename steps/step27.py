if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from step26 import *

import math

def my_sin(x, threshhold=0.0001):
    y = 0
    for i in range(100000):
        c = (-1) **i / math.factorial(2*i+1)
        t = c * x ** (2*i+1)
        y = y + t
        if abs(t.data) < threshhold:
            break
    return y