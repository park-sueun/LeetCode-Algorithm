class Solution(object):
    def __init__(self):
        self.answer = []
        self.is_positive = None
        
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_positive = True
        if x < 0:
            is_positive = False
            
        x = str(abs(x))
        answer = 0
        for idx, val in enumerate(x):
            n = int(val) * (10 ** idx)
            answer += n
        
        answer = answer if is_positive else answer * -1
        
        if is_positive:
            if answer > 2**31 - 1:
                return 0
        else:
            if answer < (2**31) * -1:
                return 0
            
        return answer