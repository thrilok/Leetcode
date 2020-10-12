class Solution:
    def removePalindromeSub(self, s: str) -> int:
        characters = list(s)
        rev_char = list(s)
        rev_char = rev_char[::-1]
        if len(characters) ==0:
            return 0
        if characters == rev_char:
            return 1
        return 2
        
# Runtime: 20 ms, faster than 97.33% of Python3 online submissions for Remove Palindromic Subsequences.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Remove Palindromic Subsequences.
# In "Example" word exe or eae are considered as the sequnece. Doesn't need to be a substring.
