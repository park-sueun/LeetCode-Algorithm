class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        flag = True
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i-1
                flag = False
                break
        if flag: nums.sort()
        else:
            swapNum = float('inf')
            swapIndex = -1
            for i in range(index+1, len(nums)):
                if nums[i] > nums[index] and swapNum > nums[index]:
                    swapNum = nums[i]
                    swapIndex = i
            temp = nums[swapIndex]
            nums[swapIndex] = nums[index]
            nums[index] = temp 
            tail = sorted(nums[index+1:])
            nums[:] = nums[:index+1] + tail