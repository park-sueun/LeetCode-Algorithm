class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        while x and len(x) != 1:
            if x.pop(0) != x.pop(-1):
                return False
        return True
            
            
        