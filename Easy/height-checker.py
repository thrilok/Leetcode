class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new = sorted(heights)
        count = 0
        length = len(heights)
        for x in range(0, length):
            if new[x] != heights[x]:
                count+=1
        return count
    
# Runtime: 48 ms, faster than 17.95% of Python3 online submissions for Height Checker.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Height Checker.
