class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        max_length = 0
        string_len = len(s)
        if string_len <=1:
            return string_len
        sub = []
        for x in range(0, string_len):
            if s[x] not in sub:
                sub.append(s[x])
            else:
                index_found = sub.index(s[x])
                sub = sub[index_found+1:]
                sub.append(s[x])
            length = len(sub)
            if max_length < length:
                max_length = length
        return max_length



# Runtime: 68 ms, faster than 61.60% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13 MB, less than 98.98% of Python3 online submissions for Longest Substring Without Repeating Characters.

