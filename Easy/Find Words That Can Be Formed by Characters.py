import copy
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        hashmap = {}
        for char in chars:
            if char in hashmap:
                hashmap[char] +=1
            else:
                hashmap[char] = 1
        for word in words:
            temp = copy.deepcopy(hashmap)
            found = True
            for char in word:
                if char in temp:
                    if temp[char]>0:
                        temp[char] -=1
                    else:
                        found = False
                        break
                else:
                    found = False
                    break
            if found:
                result += len(word)
        return result
    
# Runtime: 592 ms, faster than 5.12% of Python3 online submissions for Find Words That Can Be Formed by Characters.
# Memory Usage: 14.8 MB, less than 18.12% of Python3 online submissions for Find Words That Can Be Formed by Characters.


import copy
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        hashmap = {}
        for char in chars:
            if char in hashmap:
                hashmap[char] +=1
            else:
                hashmap[char] = 1
        for word in words:
            temp = copy.copy(hashmap)
            found = True
            for char in word:
                if char in temp:
                    if temp[char]>0:
                        temp[char] -=1
                    else:
                        found = False
                        break
                else:
                    found = False
                    break
            if found:
                result += len(word)
        return result
    
# Runtime: 88 ms, faster than 91.93% of Python3 online submissions for Find Words That Can Be Formed by Characters.
# Memory Usage: 14.8 MB, less than 18.12% of Python3 online submissions for Find Words That Can Be Formed by Characters.