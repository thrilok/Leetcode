class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_s = len(s)
        hash_table = {
        
        }
        length_t = len(t)
        for x in range(0, length_s):
            try:
                hash_table[s[x]] +=1
            except:
                hash_table[s[x]] = 1
        for x in range(0, length_t):
            try:
                hash_table[t[x]] -=1
                if hash_table[t[x]] <0:
                    return False
            except:
                return False
        values = list(hash_table.values())
        for x in range(0, len(values)):
            if values[x] >0:
                return False
        return True
        
# Runtime: 52 ms, faster than 56.87% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Valid Anagram.


