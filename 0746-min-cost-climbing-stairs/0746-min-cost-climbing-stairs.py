class Solution(object):
    def __init__(self):
        self.min_cost = {}
        
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(cost) + 1):
            if i == 0 or i == 1:
                self.min_cost[i] = 0
            else:
                self.min_cost[i] = min(
                    self.min_cost[i-1] + cost[i-1],
                    self.min_cost[i-2] + cost[i-2]
                )
        
        return self.min_cost[len(cost)]