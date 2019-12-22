class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower = 0
        higher = len(nums)-1
        found = False
        mid = int((lower+higher)/2)
        while higher >= lower:
            if nums[mid] > target:
                higher = mid-1
                mid = int((lower+higher)/2)
            elif nums[mid] < target:
                lower = mid+1
                mid = int((lower+higher)/2)
            elif nums[mid] == target:
                return mid
        if target < nums[mid]:
            if mid ==0:
                return mid
            return (mid-1)
        elif target > nums[higher]:
            return (higher+1)
        else:
            return (mid+1)

# Runtime: 48 ms, faster than 89.54% of Python3 online submissions for Search Insert Position.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Search Insert Position.


