class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = {
        
        }
        for x in arr:
            if x in hash_map:
                hash_map[x]+=1
            else:
                hash_map[x] = 1
        output = []
        for key in hash_map:
            if hash_map[key] == key:
                output.append(key)
        if len(output)==0:
            return -1
        output.sort()
        return output[len(output)-1]
    
# Runtime: 60 ms, faster than 55.31% of Python3 online submissions for Find Lucky Integer in an Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Find Lucky Integer in an Array.


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = {
        
        }
        for x in arr:
            if x in hash_map:
                hash_map[x]+=1
            else:
                hash_map[x] = 1
        output = []
        for key in hash_map:
            if hash_map[key] == key:
                output.append(key)
        if len(output)==0:
            return -1
        return max(output)

# Runtime: 56 ms, faster than 77.06% of Python3 online submissions for Find Lucky Integer in an Array.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Find Lucky Integer in an Array.

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = {
        
        }
        for x in arr:
            if x in hash_map:
                hash_map[x]+=1
            else:
                hash_map[x] = 1
        result = -1
        for key in hash_map:
            if hash_map[key] == key:
                if key > result:
                    result = key
        return result
    
# Runtime: 48 ms, faster than 97.86% of Python3 online submissions for Find Lucky Integer in an Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Find Lucky Integer in an Array.

