class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp, s_dict = [], {'(': ')', '{': '}', '[': ']'}
        
        for i in list(s):
            if i in [')', '}', ']']:
                if not temp or temp.pop() != i:
                    return False
            else:
                temp.append(s_dict[i])
        
        return False if temp else True