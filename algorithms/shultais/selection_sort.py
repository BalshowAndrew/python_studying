from random import randint

data = [randint(1, 100) for i in range(10)]

print(data)

def find_min_value(data):
    min = data[0]
    for i in range(1, len(data)):
        if data[i] < min:
            min = data[i]
    data[data.index(min)] = data[0]
    data[0] = min
    return data

# print(find_min_value(data))



def selection_sort(data):
    for i in range(len(data) - 1):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        if i != min_idx:
            data[i], data[min_idx] = data[min_idx], data[i]
            print(data) 


# def selection_sort_desc(data):
#     for n in range(len(data) - 1):
#         min = data[0]
#         for i in range(1, len(data) - n):
#             if data[i] < min:
#                 min = data[i]
#         data[data.index(min)] = data[len(data) - (n + 1)]
#         data[len(data) - (n + 1)] = min
#     return data

def selection_sort_desc(data):
    for i in range(len(data) - 1):
        min_idx = 0
        for j in range(1, len(data) - i):
            if data[min_idx] > data[j]:
                min_idx = j
        if i != min_idx:
            data[len(data) - (i + 1)], data[min_idx] = data[min_idx], data[len(data) - (i + 1)]
            print(data)



# selection_sort(data)
selection_sort_desc(data)
