import time
import numpy as np

data1 = np.arange(1, 1000_000)
data2 = np.arange(999_999, 0, -1)

def flawed(A):
    my_max = 0
    for i in A:
        if my_max < i:
            my_max = i
    return my_max

def get_time(A):
    start_time = time.time()
    print(f"Наибольшее значение: {flawed(A)}")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения алгоритма: {execution_time} секунд")


get_time(data1)
get_time(data2)
