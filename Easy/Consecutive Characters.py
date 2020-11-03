class Solution:
    def maxPower(self, s: str) -> int:
        result = 0 
        count = 0
        if len(s) ==1:
            return 1
        for x in range(1, len(s)):
            if s[x] == s[x-1]:
                if count ==0:
                    count = 2
                else:
                    count +=1
            else:
                count = 1
            if result< count:
                result = count
        return result
    
# Runtime: 40 ms, faster than 74.28% of Python3 online submissions for Consecutive Characters.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Consecutive Characters.
