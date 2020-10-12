class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        _a = ord('a')
        _z = ord('z')
        for x in s:
            temp = ord(x.lower())
            if (temp>=_a and temp<=_z) or (temp >= ord('0') and temp <= ord('9')):
                letters.append(x.lower())
        right = len(letters)-1
        left = 0
        while left<right:
            if letters[left] != letters[right]:
                return False
            else:
                left +=1
                right -=1
        return True
        
# Runtime: 56 ms, faster than 46.45% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 19 MB, less than 15.60% of Python3 online submissions for Valid Palindrome.

