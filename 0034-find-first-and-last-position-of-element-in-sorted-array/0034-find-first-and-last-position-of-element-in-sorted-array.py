class Solution(object):
    
    def findTarget(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) / 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return -1
    
    def findFirst(self, nums, target, idx):
        if idx == 0:
            return idx
        
        if nums[idx - 1] != target:
            return idx
        
        return self.findFirst(nums, target, idx - 1)
    
    def findLast(self, nums, target, idx):
        if idx == len(nums) - 1:
            return idx
        
        if nums[idx + 1] != target:
            return idx

        return self.findLast(nums, target, idx + 1)
    
                
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = self.findTarget(nums, target)
        if idx == -1:
            return [-1, -1]
        else:
            first = self.findFirst(nums, target, idx)
            last = self.findLast(nums, target, idx)
            return [first, last]
        