class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums)<3:
            return result
        length = len(nums)
        nums.sort()
        if nums[0]>0:
            return result
        print(nums)
        for i in range(0, length-2):
            target = nums[i]
            if i>0 and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = length-1
            while left<right:
                if nums[left]+ nums[right] +target ==0:
                    result.append([nums[left], nums[right], target])
                    while right>1 and nums[right] == nums[right-1]:
                        right -=1
                    while left<length-1 and nums[left] == nums[left+1]:
                        left +=1
                    left+=1
                    right-=1
                elif nums[left]+nums[right] > -target:
                    right-=1
                elif nums[left]+nums[right] < -target:
                    left+=1
        return result
    
# Runtime: 1132 ms, faster than 37.61% of Python3 online submissions for 3Sum.
# Memory Usage: 17.4 MB, less than of Python3 online submissions for 3Sum.

