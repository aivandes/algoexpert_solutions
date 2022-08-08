def firstDuplicateValue(array):
    a = {}
    if len(array) < 2:
        return -1
    for i in range(len(array)):
        if array[i] not in a:
            a[array[i]] = 1
        else:
            return array[i]
    else:
        return -1
