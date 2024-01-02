import numpy as np
from random import randint
from timing import get_time


data1 = np.arange(1, 100)
data2 = np.arange(99, 0, -1)
data3 = [randint(-100, 100) for i in range(100)]

def largest_two(A):
    max, next = A[:2]
    if max < next:
        max, next = next, max
    for i in range(2, len(A)):
        if max < A[i]:
            max, next = A[i], max
        elif next < A[i]:
            next = A[i]
    return (max, next)


get_time(largest_two(data1))

get_time(largest_two(data2))

get_time(largest_two(data3))
