import string
import math
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        alphabets = list(string.ascii_lowercase)
        total_count = {x:math.inf for x in alphabets}
        for s in A:
            count = {x:0 for x in alphabets}
            for c in s:
                count[c] +=1
            for x in alphabets:
                total_count[x] = min(total_count[x], count[x])
        result = []
        for x in alphabets:
            count = 0
            while count<total_count[x]:
                result.append(x)
                count +=1
        return result
    
# Runtime: 56 ms, faster than 48.55% of Python3 online submissions for Find Common Characters.
# Memory Usage: 13.7 MB, less than 93.94% of Python3 online submissions for Find Common Characters.
