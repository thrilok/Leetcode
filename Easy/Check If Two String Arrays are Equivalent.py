class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ''
        string2 = ''
        for x in word1:
            string1 += x
        for x in word2:
            string2 += x
        return string1 == string2

# Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Memory Usage: 14.3 MB, less than 25.00% of Python3 online submissions for Check If Two String Arrays are Equivalent.