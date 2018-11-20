'''

68. Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
     
    results = []
        
    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        self.results.append(root.val) 



    def postorderTraversal(self, root):
        self.results = []
        self.traverse(root)
        return self.results