class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        q, sum = 0, 1
        while digits:
            sum += (digits.pop() * (10 ** q))
            q += 1
            
        return [int(d) for d in list(str(sum))]
            