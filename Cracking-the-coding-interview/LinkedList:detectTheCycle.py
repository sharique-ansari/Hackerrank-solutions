"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node


    Constraints given list size <= 100
    we will exploit this fact


"""


def has_cycle(head):
    curr = head

    for i in range(100):
        curr = head.next
        if not curr:
            return False
    return True
