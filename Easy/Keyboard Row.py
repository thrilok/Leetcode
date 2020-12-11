class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        result = []
        for word in words:
            tempWord = word.lower()
            if len(word)>0:
                row = row1
                if tempWord[0] in row1:
                    row = row1
                elif tempWord[0] in row2:
                    row = row2
                elif tempWord[0] in row3:
                    row = row3
            sameRow = True
            for char in tempWord:
                if char not in row:
                    sameRow = False
                    break
            if sameRow:
                result.append(word)
        return result


# Runtime: 32 ms, faster than 41.03% of Python3 online submissions for Keyboard Row.
# Memory Usage: 14.3 MB, less than 16.23% of Python3 online submissions for Keyboard Row.