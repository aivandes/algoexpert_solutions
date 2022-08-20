def runLengthEncoding(string):
  
    curr_letter = string[0]
    counter = 1
    i = 1
    previous = ""
    res = []
    
    if len(string) < 2:
        return "1"+string[0]
        
    while i < len(string):
        previous = curr_letter
        curr_letter = string[i]
        
        if curr_letter == previous and counter < 9:
            counter += 1
            i += 1
        else:
            res.append(str(counter)+previous)    
            counter = 1
            i += 1
            
        if i == len(string):
            res.append(str(counter)+curr_letter)
            
    return "".join(res)
