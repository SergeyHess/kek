def bubleSort(arr):
    b = True
    j = 0
    while b:
        b = False
        for i in range(1, len(arr)-j):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                b = True
        j += 1
    return arr


arr_ = [64, 34, 25, 12, 22, 11, 90]
print(bubleSort(arr_))
