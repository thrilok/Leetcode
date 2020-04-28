class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        for x in range(0, len(nums)):
            if nums[x]> first:
                third = second
                second = first
                first = nums[x]
            elif nums[x]> second and nums[x]< first:
                third = second
                second = nums[x]
            elif nums[x]> third and nums[x]< second:
                third = nums[x]
        if third == float('-inf'):
            return first
        else:
            return third

# Runtime: 88 ms, faster than 5.14% of Python3 online submissions for Third Maximum Number.
# Memory Usage: 14.6 MB, less than 7.69% of Python3 online submissions for Third Maximum Number.
