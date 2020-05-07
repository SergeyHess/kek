
def binary_search(arr, value):
    top = len(arr) - 1
    bott = 0
    mid = len(a) // 2
    while arr[mid] != value and bott <= top:
        bott = mid + 1 if value > arr[mid] else top = mid - 1
        mid = (top + bott) // 2
    print('No value') if bott > top else print(mid)
