class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum = len(list1)+ len(list2)
        min_res = []
        hashmap = {}
        index = 0
        for x in list1:
            hashmap[x] = index
            index+=1
        index = 0
        for x in list2:
            if x in hashmap:
                temp = hashmap[x]+index
                if temp <minimum:
                    min_res =[x]
                    minimum = temp
                elif temp == minimum:
                    min_res.append(x)
            index+=1
        return min_res
        
# Runtime: 148 ms, faster than 76.28% of Python3 online submissions for Minimum Index Sum of Two Lists.
# Memory Usage: 14.5 MB, less than 76.35% of Python3 online submissions for Minimum Index Sum of Two Lists.
