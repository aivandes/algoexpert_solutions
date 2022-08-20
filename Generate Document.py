def generateDocument(characters, document):
    a = {}
    
    for i in characters:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1

    for x in document:
        if x not in a or a[x] == 0:
            return False
        
        a[x] -= 1

    return True
