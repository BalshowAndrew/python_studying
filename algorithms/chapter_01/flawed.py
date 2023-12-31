import numpy as np
from timing import get_time 


data1 = np.arange(1, 1000_000)
data2 = np.arange(999_999, 0, -1)

def flawed(A):
    my_max = 0
    for i in A:
        if my_max < i:
            my_max = i
    return my_max


get_time(flawed(data1))

get_time(flawed(data2))
