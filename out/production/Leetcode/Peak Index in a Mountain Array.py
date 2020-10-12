class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 0
        length = len(A)
        current = A[0]
        next_ele = A[1]
        i = 0
        while current < next_ele:
            i +=1
            current = A[i]
            next_ele = A[i+1]
        return i
        

#
# Runtime: 80 ms, faster than 97.61% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 14.2 MB, less than 78.79% of Python3 online submissions for Peak Index in a Mountain Array.



class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 0
        while A[i] < A[i+1]:
            i +=1
        return i

# Runtime: 80 ms, faster than 97.61% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 14 MB, less than 96.97% of Python3 online submissions for Peak Index in a Mountain Array.
