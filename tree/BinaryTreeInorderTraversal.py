'''
67. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.
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
    @return: Inorder in ArrayList which contains node values.
   
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val]\
            + self.inorderTraversal(root.right)
    """
    # write your code here
    def inorderTraversal(self, root):
        if not root:
            return []
        
        result = []
        stack = []
        
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            curNode = stack.pop()
            result.append(curNode.val)
            
            if curNode.right:
                curNode = curNode.right
                while curNode:
                    stack.append(curNode)
                    curNode = curNode.left
        
        return result