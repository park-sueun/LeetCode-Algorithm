class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [(idx, val) for idx, val in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[1])
        
        left, right = [0, len(nums) - 1]
        while left < right:
            curr_sum = nums[left][1] + nums[right][1]
            if curr_sum == target:
                return [nums[left][0], nums[right][0]]
            
            elif curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
                
        return []
        