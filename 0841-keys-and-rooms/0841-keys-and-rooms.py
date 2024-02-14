class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = []
        curr_v = 0 # 0번째 방은 열린 상태
        
        def dfs(curr_v):
            visited.append(curr_v)
            for v in rooms[curr_v]:
                if v not in visited:
                    dfs(v)
        
        dfs(curr_v)
        return len(visited) == len(rooms)