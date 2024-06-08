from itertools import combinations as comb

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # 1. Pascal's Triangle 구성
        dp = [[1] * i for i in range(1, numRows+1)]
		
        # 2. Dynamic Programming을 이용해 해답 구하기
        for i in range(2, numRows):
            for j in range(1, i):
                print(i, j)
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp
