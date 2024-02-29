class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost = {}
        cost.append(0)
        for i in range(1, len(cost) + 1):
            if i == 1 or i == 2:
                if i not in min_cost:
                    min_cost[i] = cost[i-1]
            else:
                min_cost[i] = min(min_cost[i-1], min_cost[i-2]) + cost[i-1]
                
        return min_cost[len(cost)]