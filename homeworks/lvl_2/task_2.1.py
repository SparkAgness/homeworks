# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    mi = arr[0]
    for c in arr:        
        if c < mi:
            mi = c
    return mi


def maximum(arr):
    ma = arr[0]
    for c in arr:
        if c > ma:
            ma = c
    return ma

arr = [4,6,2,1,9,63,-134,566]
arr2 = [-52, 56, 30, 29, -54, 0, -110]
arr3 = [42, 54, 65, 87, 0] 
arr4 = [5]

all = [arr, arr2, arr3, arr4]
for element in all:
    print(f"{element}\t -> min = {minimum(element)}, max = {maximum(element)}")
