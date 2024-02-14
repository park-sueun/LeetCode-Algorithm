class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        curr_v = 0
        
        def dfs(curr_v):
            visited.add(curr_v)
            for next_v in rooms[curr_v]:
                if next_v not in visited:
                    dfs(next_v)
        
        dfs(curr_v)
        return len(visited) == len(rooms)