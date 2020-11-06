class Solution:
    def minFlips(self, target: str) -> int:
        length = len(target)
        current = 0
        previous = "0"
        result = 0
        while current < length:
            if target[current] != previous:
                result +=1
                previous = target[current]
            else:
                current+=1
        return result
    
# Runtime: 104 ms, faster than 40.40% of Python3 online submissions for Bulb Switcher IV.
# Memory Usage: 14.7 MB, less than 5.77% of Python3 online submissions for Bulb Switcher IV.

