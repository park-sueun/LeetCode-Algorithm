# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def __init__(self):
        self.visited = []
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
            
        if root is None:
            return None
        
        left = self.inorderTraversal(root.left)
        self.visited.append(root.val)
        right = self.inorderTraversal(root.right)
        
        return self.visited