class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        i = 0
        j = length-1
        maximum_area = 0
        while i<j:
            if height[i]< height[j]:
                temp = height[i]*(j-i)
                i +=1
            else:
                temp = height[j]*(j-i)
                j -=1
            if maximum_area < temp:
                    maximum_area = temp
        return maximum_area
    
# Runtime: 160 ms, faster than 11.98% of Python3 online submissions for Container With Most Water.
# Memory Usage: 15.4 MB, less than 5.26% of Python3 online submissions for Container With Most Water.
