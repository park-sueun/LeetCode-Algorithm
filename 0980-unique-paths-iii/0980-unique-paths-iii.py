class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1:
                    todo += 1
                if val == 1:
                    sr, sc = r, c
                if val == 2:
                    tr, tc = r, c

        self.ans = 0

        def dfs(r, c, todo):
            todo -= 1
            if r == tr and c == tc:
                if todo == 0:
                    self.ans += 1
                return
            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0

        dfs(sr, sc, todo)
        return self.ans