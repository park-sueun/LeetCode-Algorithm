class Solution(object):
    def __init__(self):
        self.min_cost = {0:0, 1:0}
        
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n not in self.min_cost:
            self.min_cost[n] = min(
                self.minCostClimbingStairs(cost[:-1]) + cost[n-1],
                self.minCostClimbingStairs(cost[:-2]) + cost[n-2]
            )
        
        return self.min_cost[n]
    
#         for i in range(2, len(cost) + 1):
#             self.min_cost[i] = min(
#                 self.min_cost[i-1] + cost[i-1],
#                 self.min_cost[i-2] + cost[i-2]
#             )
        
#         return self.min_cost[len(cost)]