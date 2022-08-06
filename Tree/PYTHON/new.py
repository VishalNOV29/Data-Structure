# # Binary Tree in Python

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

#     # Traverse postorder

#     def traversePostOrder(self):
#         if self.left:
#             self.left.traversePostOrder()
#         if self.right:
#             self.right.traversePostOrder()
#         print(self.val, end=' ')
        
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.right.right.left = Node(10)
# root.right.right.right = Node(11)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.right.left = Node(9)
# root.left.left.left = Node(8)
# root.traversePostOrder()

import imp
import numpy
from tkinter imp 