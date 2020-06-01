class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {
        
        }
        for x in magazine:
            if x in hash_map:
                hash_map[x] +=1
            else:
                hash_map[x] = 1
        for x in ransomNote:
            if x in hash_map:
                hash_map[x] -=1
            else:
                return False
            if hash_map[x] <0:
                return False
        return True
    
#
