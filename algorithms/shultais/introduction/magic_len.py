# Попробуем со списками и массивами:
import numpy as np
from random import randint

arr = np.arange(0, 100)
st = [randint(1, 10) for i in range(0, 100)]


print (len(arr), arr.__len__())
print()
print(len(st), st.__len__())
