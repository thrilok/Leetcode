class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        noOfWords = len(words)
        for x in range(0, noOfWords):
            i = 0
            j = len(words[x])-1
            word = list(words[x])
            while i <j:
                temp = word[i]
                word[i] = word[j]
                word[j] = temp
                i +=1
                j -=1
            words[x] = ''.join(word)
        result = " ".join(words)
        return result
    
# Runtime: 72 ms, faster than 19.08% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.3 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.



class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        noOfWords = len(words)
        for x in range(0, noOfWords):
            words[x] = words[x][::-1]
        return (' '.join(words))
    
# Runtime: 44 ms, faster than 50.22% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.5 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
