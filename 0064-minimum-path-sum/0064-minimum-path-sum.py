class Solution(object):
    def __init__(self):
        self.path_sum = {}
        self.grid = None
        
    def get_path_sum(self, r, c):
        
        if (r, c) not in self.path_sum:
            self.path_sum[(r, c)] = min(
                self.get_path_sum(r-1, c) + self.grid[r][c],
                self.get_path_sum(r, c-1) + self.grid[r][c]
            )
            
        return self.path_sum[(r, c)]
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.path_sum[(0, 0)] = grid[0][0]
        
        for r in range(1, len(grid)):
            self.path_sum[(r, 0)] = self.path_sum[(r-1, 0)] + grid[r][0]
            
        for c in range(1, len(grid[0])):
            self.path_sum[(0, c)] = self.path_sum[(0, c-1)] + grid[0][c]
            
        return self.get_path_sum(len(grid)-1, len(grid[0])-1)