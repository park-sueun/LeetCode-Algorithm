class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: 
            return s
        
        group = (numRows - 1) * 2
        ans = ''
        
        for i in range(0, numRows):
            for j, val in enumerate(s):
                if j % group == i or j % group == group - i:
                    ans += val
                    
        return ans