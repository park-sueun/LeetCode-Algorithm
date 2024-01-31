class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            nums_dict = {n: 1 for n in nums}
            nums.sort()
            
            next_n = nums[0]
            for n in nums:
                if n >= next_n:
                    next_n = n + 1
                    while next_n in nums_dict:
                        nums_dict[n] += 1
                        next_n += 1

            return max(nums_dict.values())
        else:
            return 0
