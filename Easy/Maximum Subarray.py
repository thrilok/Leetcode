class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Maximum = [nums[0]]
        length = len(nums)
        for x in range(1, length):
            temp = Maximum[x-1]+nums[x]
            if nums[x] < temp:
                Maximum.append(temp)
            else:
                Maximum.append(nums[x])
        return max(Maximum)

# Dynamic Programming
