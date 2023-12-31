import numpy as np
from timing import get_time

data1 = np.arange(1, 4097)
data2 = np.arange(4096, 0, -1)

def alternate(A):
    for i in A:
        for j in A:
            if i < j:
                break
        else:
            return i
    return None


get_time(alternate(data1))
get_time(alternate(data2))
get_time(alternate([]))

