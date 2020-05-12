def ArithGeoII(arr):
    if len(arr) > 2:
        for i in range(1, len(arr)):
            if not (arr[i] - arr[i-1] == arr[1] - arr[0]):
                for i in range(1, len(arr)):
                    if not (arr[i]/arr[i-1] == arr[1]/arr[0]):
                        return -1
                return "Geometric"
        return "Arithmetic"
    return -1

arr_ = [2, 4, 8]

print(ArithGeoII(arr_))
