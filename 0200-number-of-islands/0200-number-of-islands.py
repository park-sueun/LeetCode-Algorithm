class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        number_of_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def bfs(x, y):
            # 암시적 그래프 문제이기 때문에 방향이 주어지지 않음
            # 따라서 dx, dy로 그래프의 방향을 나타내줘야 함: 상/하/좌/우 + alpha
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            visited[x][y] = True            # 현재 vertex에 방문함
            queue = deque()
            queue.append((x, y))            # 2차원 배열이기 때문에 (x, y) 
            
            while queue:
                curr_x, curr_y = queue.popleft()
                
                for i in range(4): # 상하좌우(4)
                    next_x = curr_x + dx[i]
                    next_y = curr_y + dy[i]
                    
                    # 그래프의 범위를 벗어나지 않도록 조건을 걸어준다
                    if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols:
                        # 다음 vertex가 땅(1)이면서 방문하지 않은(False)인 경우만 탐색 
                        if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            queue.append((next_x, next_y))
    
        # 전체 지도를 순회하면서 땅이면서 방문하지 않은 vertex가 있다면 bfs로 땅을 방문하ㅗㄱ
        # number of islands의 값을 +1 해준다.
        for row in range(rows):
            for col in range(cols):
                # 땅이면서 방문을 안했을 때
                if grid[row][col] == '1' and not visited[row][col]:
                    bfs(row, col)
                    number_of_islands += 1
        
        return number_of_islands