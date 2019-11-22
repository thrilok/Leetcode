class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        current_index = 0
        length = len(nums)
        if length ==1:
            return 0
        if nums[current_index] > nums[current_index+1]:
            return 0
        current_index = 1
        while current_index<length-1:
            if nums[current_index-1]<nums[current_index] and nums[current_index]>nums[current_index+1]:
                return current_index
            current_index+=2
        if current_index == length-1 and nums[current_index]> nums[current_index-1]:
            return current_index
        
        
        
# Runtime: 48 ms, faster than 93.70% of Python3 online submissions for Find Peak Element.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Peak Element.
