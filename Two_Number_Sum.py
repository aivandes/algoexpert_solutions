def twoNumberSum(array, targetSum):
    map = {}
    for i,n in enumerate(array):
        if targetSum - array[i] in map:
            return [array[i],(targetSum - array[i])]
        map[n] = i
    else:
        return []