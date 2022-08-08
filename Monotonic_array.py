def isMonotonic(array):

    minus = 0
    plus = 0
    finish = len(array)
    if len(array) < 2:
        return True
    for i in range(finish-1):
        if array[i+1] > array[i]:
            plus += 1
        elif array[i+1] < array[i]:
            minus += 1
        else:
            minus += 1
            plus += 1

    return True if minus + 1 == finish or plus+1 == finish else False
