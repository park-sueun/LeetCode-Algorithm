class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [(i, nums[i]) for i in range(len(nums))]
        nums = sorted(nums, key=lambda x:x[1])
        
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l][1] + nums[r][1] > target:
                r -= 1
            elif nums[l][1] + nums[r][1] < target:
                l += 1
            else:
                return [nums[l][0], nums[r][0]]

        