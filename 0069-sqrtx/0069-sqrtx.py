class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0
        elif x == 1:
            return 1
        
        i = 2
        while(1):
            if i * i > x:
                return i - 1
            i += 1
                
        return result