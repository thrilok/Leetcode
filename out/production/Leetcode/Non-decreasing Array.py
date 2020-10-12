class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        output = True
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                if output == True:
                    output = False
                else:
                    return False
                if i>0:
                    if nums[i-1]> nums[i+1]:
                        nums[i+1] = nums[i]
        return True

# Runtime: 288 ms, faster than 7.76% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 15.2 MB, less than 6.67% of Python3 online submissions for Non-decreasing Array.
