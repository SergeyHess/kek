def HDistance(strArr):
    counter = 0
    for i_1, i_2 in zip(strArr[0],strArr[1]):
        if i_1 != i_2:
            counter += 1
    return counter
