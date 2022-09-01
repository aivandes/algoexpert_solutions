#No usage of split or Reverse and O(n) time and O(n) space

def reverseWordsInString(string):
    stack = []
    i = j = 0
    res = []
    
    if len(string) == 1:
        return string

    while i < len(string) and j < len(string):
        j = i
            
        if string[i] == " ":
            while j < len(string) and string[j] == " ":
                j += 1
            stack.append(" "*(j - i))
            i = j

        elif string[i] != " ":
            while j < len(string) and string[j] != " ":
                j += 1
            stack.append(string[i:j])
            i = j

    for _ in range(len(stack)):
        res.append(stack.pop())

    return "".join(res)
