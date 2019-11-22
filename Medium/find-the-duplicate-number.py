class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        print(length)
        hash_table = {}
        for x in range (0, length):
            hash_table[x] = 0
        for x in range(0, length):
            try:
                hash_table.pop(nums[x])
            except:
                return nums[x]
            
# Runtime: 80 ms, faster than 63.86% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 17.6 MB, less than 7.14% of Python3 online submissions for Find the Duplicate
