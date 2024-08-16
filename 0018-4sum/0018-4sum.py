class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums) -2):
                
                l, r = j+1, len(nums) -1
                check = target - nums[i] - nums[j]
                
                while l < r:
                    if nums[l] + nums[r] == check:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                    
                    if nums[l] + nums[r] > check:
                        r -= 1
                    else: #nums[l] + nums[r] < check:
                        l += 1
        
        return res