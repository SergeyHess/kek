def ArithGeoII(arr):
    for i in range(1, len(arr)):
        if not (arr[i] - arr[i-1] == arr[1] - arr[0]):
            for i in range(1, len(arr)):
                if not (arr[i]/arr[i-1] == arr[1]/arr[0]):
                    return -1
            return "Geometric"
    return "Arithmetic"
