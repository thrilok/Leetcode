class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ['']*len(s)
        count = 0
        for x in indices:
            result[x] = s[count]
            count+=1
        return(''.join(result))
        
# Runtime: 48 ms, faster than 94.57% of Python3 online submissions for Shuffle String.
# Memory Usage: 14 MB, less than 99.99% of Python3 online submissions for Shuffle String.
