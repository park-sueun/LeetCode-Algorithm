# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def __init__(self):
        self.root = None
        self.left_visited = []
        self.right_visited = []
        
    def left_traversal(self, root):
        if root is None:
            self.left_visited.append(None)
            return None
        
        self.left_visited.append(root.val)
        self.left_traversal(root.left)
        self.left_traversal(root.right)
    
    
    def right_traversal(self, root):
        if root is None:
            self.right_visited.append(None)
            return None
        
        self.right_visited.append(root.val)
        self.right_traversal(root.right)
        self.right_traversal(root.left)
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.root is None:
            self.root = root
        
        if root is None:
            return None
        
        self.left_traversal(root.left)
        self.right_traversal(root.right)
        
        return self.left_visited == self.right_visited
        
        