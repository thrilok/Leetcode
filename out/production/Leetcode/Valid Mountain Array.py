class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        increasing = False
        decreasing = False
        for x in range(1, len(A)):
            if A[x-1]<A[x] and decreasing == False:
                increasing = True
            elif A[x-1]>A[x] and increasing == True:
                decreasing = True
            else:
                return False
        if increasing == True and decreasing == True:
            return True
        return False

# Runtime: 212 ms, faster than 85.83% of Python3 online submissions for Valid Mountain Array.
# Memory Usage: 15.1 MB, less than 5.26% of Python3 online submissions for Valid Mountain Array.
