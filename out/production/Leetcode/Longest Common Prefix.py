class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        length = len(strs)
        try:
            minimum_length = len(strs[0])
            for x in range(0, minimum_length):
                character = strs[0][x]
                for y in range(1, length):
                    if character != strs[y][x]:
                        return answer
                answer += character
        except:
            return answer
        return answer

# Runtime: 36 ms, faster than 36.23% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        answer = strs[0]
        for x in range(1, len(strs)):
            answer = self.compareString(answer, strs[x])
        return answer
    def compareString (self, str1, str2):
        result = ''
        i = 0
        j = 0
        len1 = len(str1)
        len2 = len(str2)
        while i < len1 and j <len2:
            if str1[i] != str2[j]:
                return result
            result += str1[i]
            i +=1
            j +=1
        return result
    
# Runtime: 40 ms, faster than 21.42% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
