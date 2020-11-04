class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        count = 0
        length = len(nums)
        if length ==1:
            return 1
        for x in range(1, length):
            if nums[x] > nums[x-1]:
                count +=1
            else:
                count = 0
            if result < count +1:
                result = count +1
        return result
   
# Runtime: 72 ms, faster than 80.53% of Python3 online submissions for Longest Continuous Increasing Subsequence.
# Memory Usage: 15.3 MB, less than 100.00% of Python3 online submissions for Longest Continuous Increasing Subsequence.
