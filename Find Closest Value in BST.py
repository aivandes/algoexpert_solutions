def findClosestValueInBst(tree, target):
    curr_value = tree
    diff_min = float("inf")
    res = 0
    while curr_value:
        
        if curr_value.value < target:
            diff_curr = abs(target - curr_value.value)
            
            if diff_curr < diff_min:
                diff_min = diff_curr
                res = curr_value.value
            curr_value = curr_value.right
            
        elif curr_value.value > target:
            diff_curr = abs(target - curr_value.value)

            if diff_curr < diff_min:
                diff_min = diff_curr
                res = curr_value.value
            curr_value = curr_value.left
        else:
            return curr_value.value
    return res
            
            


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
