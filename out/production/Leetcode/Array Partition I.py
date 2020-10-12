class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        result = 0
        for x in range(0, length, 2):
            result = result + nums[x]
        return result

# Runtime: 296 ms, faster than 44.15% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.2 MB, less than 6.06% of Python3 online submissions for Array Partition I.
# Time complexity (n logn)

