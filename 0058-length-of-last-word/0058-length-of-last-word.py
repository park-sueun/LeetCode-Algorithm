class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s_list = s.split(" ")
        result = [s for s in s_list if s]
        return len(list(result[-1]))