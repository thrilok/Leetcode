class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for x in A:
            x.reverse()
            for y in range(0, len(x)):
                if x[y] == 0:
                    x[y] = 1
                else:
                    x[y] = 0
        return A
        
# Runtime: 52 ms, faster than 53.41% of Python3 online submissions for Flipping an Image.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Flipping an Image.

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for x in A:
            x.reverse()
            row_len = len(x)
            for y in range(0, row_len):
                x[y] = x[y]^1
        return A
        
# Runtime: 52 ms, faster than 53.41% of Python3 online submissions for Flipping an Image.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Flipping an Image.
