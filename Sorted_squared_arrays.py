def sortedSquaredArray(array):
    
    a =[0]*len(array)
    
    smaller = array[0]
   
    bigger = array[-1]

    r = -1
    l = 0
    for _ in range(len(array)):
        
        if abs(array[l])<=abs(array[r]):
            bigger, smaller = array[r], array[l]
            a[len(array)+r-l] = bigger**2

            r -=1
            
        else:
            bigger, smaller = array[l], array[r]
            a[len(array)+r-l] = bigger**2
            
            l += 1

    return a