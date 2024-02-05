class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cnt = 0
        nums_set = set(nums)
        for curr_num in nums_set:
            prev_num, next_num = [curr_num - 1, curr_num + 1]
            curr_cnt = 1
            if prev_num not in nums_set: # First Start Numer!
                while next_num in nums_set:
                    curr_cnt += 1
                    next_num += 1
            max_cnt = max(max_cnt, curr_cnt)
        
        return max_cnt
