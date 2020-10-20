class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)<2:
            return -1
        first_max = float(-inf)
        second_max = float(-inf)
        for x in nums:
            if x>= first_max:
                second_max= first_max
                first_max = x
            if second_max<x<first_max:
                second_max= x
        return((first_max-1)*(second_max-1))

# Runtime: 48 ms, faster than 84.36% of Python3 online submissions for Maximum Product of Two Elements in an Array.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Maximum Product of Two Elements in an Array.

