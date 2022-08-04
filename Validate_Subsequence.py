def isValidSubsequence(array, sequence):
    x = 0
    for i in array:
        if i == sequence[x]:
            x += 1
        if x == len(sequence):
            return True
    else:
        return False
        