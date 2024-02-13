class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        shortest_path_len = -1
        row = len(grid)
        col = len(grid[0])
        
        # 시작점 또는 도착점이 없는 경우는 -1을 반환
        if grid[0][0] != 0 or grid[row-1][col-1] != 0:
            return shortest_path_len
        
        # 방문 여부 체크용
        visited = [[False] * col for _ in range(row)]
        
        # 각 vertex에서 갈 수 있는 방향(상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
        directions = [
            (0, -1), (0 , 1), (-1, 0), (1, 0),
            (-1, -1), (1, -1), (-1, 1), (1, 1)
        ]
        
        queue = deque()
        queue.append((0, 0, 1)) # start_x, start_y, path_len
        visited[0][0] = True
        
        while queue:
            curr_x, curr_y, path_len = queue.popleft()
            # 가장 먼저 curr_x, curr_y의 좌표가 도착 좌표와 같은 경우 최단 거리로 도착한 path 이므로
            # 다음 과정을 진행하지 않고 반복문을 종료한다
            if curr_x == row - 1 and curr_y == col - 1:
                shortest_path_len = path_len
                break
            
            for dx, dy in directions:
                next_x = curr_x + dx
                next_y = curr_y + dy
                
                # next_x, next_y가 grid의 범위를 넘지 않아야 함
                if row > next_x >= 0 and col > next_y >= 0:
                    # 1. next grid의 값이 0이어야만 길로 취급(문제에서 그랬음)
                    # 2. 방문한 적이 없어야 함
                    if grid[next_x][next_y] == 0 and visited[next_x][next_y] != True:
                        queue.append((next_x, next_y, path_len + 1))
                        visited[next_x][next_y] = True
                        
        return shortest_path_len