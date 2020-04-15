class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        length = len(paragraph)
        banned_words = set(banned)
        character = string.ascii_lowercase + string.ascii_uppercase
        words  = []
        hash_set  = {
        
        }
        temp_word = ''
        for x in range(0, length):
            if paragraph[x] in character:
                temp_word += paragraph[x]
            else:
                if len(temp_word)>0:
                    words.append(temp_word.lower())
                    temp_word = ''
        if len(temp_word)>0:
            words.append(temp_word.lower())
        result_word = ''
        maximum = 0
        print(words)
        for x in range(0, len(words)):
            current_word = words[x]
            try:
                hash_set[current_word] +=1
            except:
                hash_set[current_word] = 1
            if hash_set[current_word] > maximum and current_word not in banned_words:
                result_word = current_word
                maximum = hash_set[current_word]
        return result_word
        
# Runtime: 40 ms, faster than 23.28% of Python3 online submissions for Most Common Word.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Most Common Word.


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        length = len(paragraph)
        banned_words = set(banned)
        character = string.ascii_lowercase + string.ascii_uppercase
        words = []
        hash_set = {

        }
        temp_word = ''
        for x in range(0, length):
            if paragraph[x] in character:
                temp_word += paragraph[x].lower()
            else:
                if len(temp_word)>0:
                    if temp_word not in banned_words:
                        words.append(temp_word)
                    temp_word = ''
        if len(temp_word)>0:
            if temp_word not in banned_words:
                words.append(temp_word)
        result_word = ''
        maximum = 0
        print(words)
        for x in range(0, len(words)):
            current_word = words[x]
            try:
                hash_set[current_word] +=1
            except:
                hash_set[current_word] = 1
            if hash_set[current_word] > maximum:
                result_word = current_word
                maximum = hash_set[current_word]
        return result_word

# Runtime: 32 ms, faster than 70.23% of Python3 online submissions for Most Common Word.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Most Common Word.
