class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        for x in nums:
            if nums[abs(x)-1] >0:
                nums[abs(x)-1] = 0-nums[abs(x)-1]
        length = len(nums)
        for x in range(0, length):
            if nums[x]>0:
                answer.append(x+1)
        return answer
    
# Runtime: 424 ms, faster than 23.46% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 21.5 MB, less than 17.86% of Python3 online submissions for Find All Numbers Disappeared in an Array.

