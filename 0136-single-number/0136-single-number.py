from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = defaultdict(int)
        for n in nums:
            nums_dict[n] += 1
            
        answer = [
            key for key, value in nums_dict.items() if value == 1
        ]
        
        return answer[0]