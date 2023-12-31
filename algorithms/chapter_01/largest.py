import numpy as np
from timing import get_time

data1 = np.arange(1, 1_000_000)
data2 = np.arange(999_999, 0, -1)

def largest(A):
    max_val = A[0]
    for i in range(1, len(A)):
        if max_val < i:
            max_val = i
    return max_val


get_time(largest(data1))
get_time(largest(data2))
get_time(largest([]))
