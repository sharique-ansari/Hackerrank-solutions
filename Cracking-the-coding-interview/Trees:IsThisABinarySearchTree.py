""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
Max = 100000000000
Min = -100000000000


def checkBST(root):
    return isBSTutil(root, Min, Max)


def isBSTutil(root, min, max):
    if root is None:
        return True
    if root.data < min or root.data > max:
        return False
    return isBSTutil(root.left, min, root.data - 1) and isBSTutil(root.right, root.data + 1, max)
