class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        x = 0
        while x <length:
            if arr[x] == 0:
                arr.insert(x+1, 0)
                arr.pop()
                x+=2
            else:
                x+=1
            
# Runtime: 64 ms, faster than 96.97% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Duplicate Zeros.

