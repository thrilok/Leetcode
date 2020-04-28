class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ''
        space_occured = False
        for x in s:
            if ord(x)>=97 and ord(x)<=122:
                if space_occured == False:
                    word += x
                if space_occured == True:
                    word = ''
                    space_occured = False
                    word += x
            if ord(x)>=65 and ord(x)<=90:
                if space_occured == False:
                    word += x
                if space_occured == True:
                    word = ''
                    space_occured = False
                    word += x
            if ord(x)== 32:
                space_occured = True
        return len(word)

# Runtime: 48 ms, faster than 5.39% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Length of Last Word.
