class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_list = list(str(x))
        y_list = []
        while 1:
            if (len(x_list) <= len(y_list)):
                break;
            y_list.append(x_list.pop())
        
        if (len(x_list) == (len(y_list) - 1)):
            y_list.pop()
            
        return x_list == y_list
            
            
        