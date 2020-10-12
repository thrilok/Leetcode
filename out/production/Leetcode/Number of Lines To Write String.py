class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines = 0
        units = 0
        ord_a = ord('a')
        for x in S:
            current = widths[ord(x)-ord_a]
            if units+current > 100:
                lines +=1
                units = current
            else:
                units+=current
        return [lines+1, units]
    
# Runtime: 56 ms, faster than 7.29% of Python3 online submissions for Number of Lines To Write String.
# Memory Usage: 14 MB, less than 16.75% of Python3 online submissions for Number of Lines To Write String.
