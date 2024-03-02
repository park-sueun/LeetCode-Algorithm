class Solution(object):
    def __init__(self):
        self.paths = {}
        self.obstacle_grid = None
        
    def dfs(self, r, c):
        if self.obstacle_grid[r][c] == 1:
            return 0
        
        if r == 0 and c == 0:
            return 1
        
        if r < 0 or c < 0:
            return 0
        
        if (r, c) not in self.paths:
            self.paths[(r, c)] = self.dfs(r-1, c) + self.dfs(r, c-1)
            
        return self.paths[(r, c)]
        
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.obstacle_grid = obstacleGrid
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        return self.dfs(row-1, col-1)