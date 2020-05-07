def isertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


arr_ = [12, 11, 13, 5, 6]
for i in range(1, len(arr_)):
    print(arr_[i])
print(isertionSort(arr_))
