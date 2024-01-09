class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for i in list(s):
            if i in [')', '}', ']']:
                if stack == [] or (stack and c_dict[stack.pop()] != i):
                    return False
            else:
                stack.append(i)
                
        return False if stack else True