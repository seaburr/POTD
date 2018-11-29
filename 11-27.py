'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
root
'''


def serialize(node, serialized_node=None):
    if serialized_node is None:
        serialized_node = []
    while type(node.left) is Node or type(node.right) is Node:
        serialized_node = serialize(node, serialized_node)
    serialized_node.append(node.val)
    serialized_node.append(node.left)
    serialized_node.append(node.right)
    return serialized_node


def deserialize(node):
    for n in node:
        pass





'''
    root
    /  \
  left right
  /
left.left 
'''

simple_node = Node(1, 2, 3)
print(serialize(simple_node))




node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
