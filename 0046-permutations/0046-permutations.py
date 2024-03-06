class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        
        def backtrack(curr=[]):
            if len(curr) == len(nums):
                answer.append(curr[:])
            else:
                for num in nums:
                    if num not in curr:
                        curr.append(num)
                        backtrack(curr)
                        curr.pop()
                        
            return
        
        backtrack()
        return answer
            
            