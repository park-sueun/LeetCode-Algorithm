class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        answer = []
        
        def backtrack(curr=[]):
            if len(curr) == len(nums):
                next_purmute = [val for idx, val in curr]
                if next_purmute not in answer:
                    answer.append([val for idx, val in curr])
            else:
                for idx, num in enumerate(nums):
                    if (idx, num) not in curr:
                        curr.append((idx, num))
                        backtrack(curr)
                        curr.pop()
        
        backtrack()
        return answer