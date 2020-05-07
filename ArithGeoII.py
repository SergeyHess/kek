def ArithGeoII(arr):
    for i in range(1, len(arr)):
        if not (arr[i] - arr[i-1] == arr[1] - arr[0]):
            for i in range(1, len(arr)):
                if not (arr[i]/arr[i-1] == arr[1]/arr[0]):
                    return -1
            return "Geometric"
    return "Arithmetic"


arr_1 = [1, 2, 3, 4, 5, 6]
arr_2 = [-5, -15, -45]
arr_3 = [3, 7, 0]
print(ArithGeoII(arr_1))
print(ArithGeoII(arr_2))
print(ArithGeoII(arr_3))
