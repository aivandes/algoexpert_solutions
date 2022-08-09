class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sum = []
    branchSumsHelper(root, 0, sum)
    return sum


def branchSumsHelper(node, runningsum, sum):
    if node is None:
        return
    sumhelper = node.value + runningsum
    if node.left is None and node.right is None:
        sum.append(sumhelper)

    branchSumsHelper(node.left, sumhelper, sum)
    branchSumsHelper(node.right, sumhelper, sum)
