class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        
        mid = len(nums) // 2
        if len(nums) % 2 != 0:
            print(nums[mid])
            return nums[mid]
        else:
            target = [nums[mid], nums[mid - 1]]
            print(nums[mid - 1], nums[mid], sum(target), float(sum(target)) / float(len(target)))
            return float(sum(target)) / float(len(target))