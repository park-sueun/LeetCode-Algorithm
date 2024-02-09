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
        
    def isSymmetricHelper(self, left, right):
        if left is None or right is None:
            return left == right
        
        if left.val != right.val:
            return False
        
        return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root is None or self.isSymmetricHelper(root.left, root.right)