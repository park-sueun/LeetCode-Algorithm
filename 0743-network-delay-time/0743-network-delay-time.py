class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = {}
        for start, end, time in times:
            if start not in graph:
                graph[start] = []
            
            graph[start].append((time, end))
            
        pq = []
        heapq.heappush(pq, (0, k))
        
        times = {}
        last_v = None
        while pq:
            curr_time, curr_v = heapq.heappop(pq)
            
            if curr_v not in times:
                times[curr_v] = curr_time
                last_v = curr_v
                
                if curr_v in graph:
                    for time, next_v in graph[curr_v]:
                        next_time = curr_time + time
                        heapq.heappush(pq, (next_time, next_v))
                    
        return times[last_v] if len(times) == n else -1