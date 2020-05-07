def DistinctList(arr):
    counter = 0
    for i in range(len(arr)):
        if arr.count(arr[i]) > counter and arr.count(arr[i]) > 1:
            counter = arr.count(arr[i])
    return counter


arr_1 = [2, 2, 2, 2, 2, 3]
print(DistinctList(arr_1))
