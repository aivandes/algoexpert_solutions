class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current_child = queue.pop(0)
            array.append(current_child.name)
            for child in current_child.children:
                queue.append(child)
        return array
