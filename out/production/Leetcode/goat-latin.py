	class Solution:
    def toGoatLatin(self, S: str) -> str:
        sentence = S.split(" ")
        vowels = ['a', 'e','i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        total_words = len(sentence)
        for x in range(0, total_words):
            word = sentence[x]
            if word[0] in vowels:
                word = word+"ma"+("a"*(x+1))
            else:
                word = word[1:]+word[0]+"ma"+("a"*(x+1))
            sentence[x] = word
        return ' '.join(sentence)
        
        
# Runtime: 32 ms, faster than 92.65% of Python3 online submissions for Goat Latin.
# Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Goat Latin.
