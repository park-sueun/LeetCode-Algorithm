class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append((time, end))
            
        pq = []
        heapq.heappush(pq, (0, k))
        
        times = {}
        while pq:
            curr_time, curr_v = heapq.heappop(pq)
            
            if curr_v not in times:
                # 처음 방문한 경우
                times[curr_v] = curr_time
                
                if curr_v in graph:
                    for time, next_v in graph[curr_v]:
                        next_time = curr_time + time
                        heapq.heappush(pq, (next_time, next_v))
                    
        return max(times.values()) if len(times) == n else -1