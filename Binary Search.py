def binarySearch(array, target):      
        
    left = 0
    right = len(array) - 1
    
    while left <= right:
        middle = (left + right) // 2
        if target < array[middle]: 
            right = middle - 1
            
        elif target > array[middle]:
            left = middle + 1
            
        elif target == array[middle]:
            return middle

        
    else:
        return -1
