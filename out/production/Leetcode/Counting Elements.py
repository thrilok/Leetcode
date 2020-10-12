class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = {
        
        }
        for x in arr:
            if x in hash_set:
                hash_set[x] +=1
            else:
                hash_set[x] = 1
        count = 0
        for key in hash_set:
            if (key+1) in hash_set:
                count+=hash_set[key]
        return count
