class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1]*(length)
        right = [1]*(length)
        for x in range(0, length-1):
            left[x+1] = nums[x]*left[x]
        for x in range(length-1, 0, -1):
            right[x-1] = nums[x]*right[x]
        output = []
        
        for x in range(0, length):
            output.append(left[x]*right[x])
        return output
    
# Time complexity O(n)
# Space complexity O(n)
