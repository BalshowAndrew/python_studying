from random import randint
import numpy as np

arr_asc = np.arange(0, 100)
arr_desc = np.arange(99, 0, -1)
lst = [randint(0, 99) for i in range(100)]

def linear_search_enum(data, target):
    for n, v in enumerate(data):
        if v == target:
            return n
    return -1


def linear_search(data, target):
    n = 0
    while n < data.__len__():
        if data[n] == target:
            return n
        n += 1
    return -1


def linear_search_sorted(data, target):
    n = 0
    while n < len(data):
        if data[n] == target:
            return n
        if data[n] > target:
            return -1
        n += 1
    return -1

print(linear_search_enum(arr_asc, 88),
      linear_search_enum(arr_desc, 88),
      linear_search_enum(lst, 88))

print(linear_search(arr_asc, 88),
      linear_search(arr_desc, 88),
      linear_search(lst, 88))

print(linear_search_sorted(arr_asc, 88),
      linear_search_sorted(arr_desc, 88),
      linear_search_sorted(lst, 88))











