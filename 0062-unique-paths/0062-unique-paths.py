class Solution(object):
    def __init__(self):
        self.unique_paths = {}
    
    def dfs(self, row, col):
            if row <= 0 or col <= 0:
                return 1

            if (row, col) not in self.unique_paths:
                self.unique_paths[(row, col)] = self.dfs(row-1, col) + self.dfs(row, col-1)

            return self.unique_paths[(row, col)]
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
    
        return self.dfs(m-1, n-1)