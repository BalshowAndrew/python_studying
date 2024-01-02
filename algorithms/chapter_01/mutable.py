from random import randint

def mutable(A):
    idx = max(range(len(A)), key=A.__getitem__)
    my_max = A[idx]
    return my_max, idx


data = [randint(-100, 100) for i in range(10)]


print(data)
print(mutable(data))
