class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license = {
            
        }
        licensePlate = licensePlate.lower()
        for char in licensePlate:
            if 'a'<=char<='z' or 'A'<=char<='Z':
                if char in license:
                    license[char] +=1
                else:
                    license[char] =1
        result = ''
        for word in words:
            temp = copy.copy(license)
            for char in word:
                if char in temp:
                    temp[char] -=1
            allUsed = True
            for key, value in temp.items():
                if value >0:
                    allUsed = False
            if allUsed :
                if result == '' or len(result)> len(word):
                    result = word                    
        return result

# Runtime: 72 ms, faster than 72.56% of Python3 online submissions for Shortest Completing Word.
# Memory Usage: 14.7 MB, less than 9.36% of Python3 online submissions for Shortest Completing Word.