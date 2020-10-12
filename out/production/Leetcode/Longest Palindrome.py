class Solution:
    def longestPalindrome(self, s: str) -> int:
        keys = {
        }
        length = len(s)
        for x in range(0, length):
            try:
                keys[s[x]] +=1
            except:
                keys[s[x]] = 1
        odd = [0]
        result = 0
        for k, v in keys.items():
            if v%2 == 0:
                result+=v
            else:
                odd.append(v)
        odd.sort(reverse=True)
        result += odd[0]
        for x in range(1, len(odd)-1):
            result= result+(odd[x]-1)
        return result
        
# Runtime: 24 ms, faster than 94.26% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        keys = {
        }
        length = len(s)
        for x in range(0, length):
            try:
                keys[s[x]] +=1
            except:
                keys[s[x]] = 1
        result = 0
        odd_entered = False
        for k, v in keys.items():
            if v%2 == 0:
                result+=v
            else:
                odd_entered = True
                result+= (v-1)
        if odd_entered:
            return result+1
        return result
    
# Runtime: 32 ms, faster than 54.61% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.
