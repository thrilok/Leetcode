class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        return ' '.join(s[::-1])
        
# Runtime: 28 ms, faster than 84.47% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.3 MB, less than 27.04% of Python3 online submissions for Reverse Words in a String.


class Solution:
    def reverseWords(self, s: str) -> str:
        ch_index = 0
        result = ''
        while ch_index <len(s):
            if s[ch_index] != ' ':
                i = ch_index
                j = i+1
                while j < len(s):
                    if s[j] != ' ':
                        j+=1
                    else:
                        break
                if result == '':
                    result = s[i:j]
                else:
                    result = s[i:j] + " "+ result
                ch_index = j
            ch_index +=1
        return result
    
# Runtime: 40 ms, faster than 31.52% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.4 MB, less than 27.04% of Python3 online submissions for Reverse Words in a String.
