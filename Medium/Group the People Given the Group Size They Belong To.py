class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        max_groupsize = max(groupSizes)
        n = len(groupSizes)
        result = {x :[] for x in range (0, max_groupsize+1)}
        for x in range(0, n):
            result[groupSizes[x]].append(x)
        final_result = []
        for x in range(0, max_groupsize+1):
            length = len(result[x])
            if length>0:
                temp = [result[x][y:y+x] for y in range(0, length, x)]
                final_result.extend(temp)
        return final_result
        
# Runtime: 76 ms, faster than 77.66% of Python3 online submissions for Group the People Given the Group Size They Belong To.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Group the People Given the Group Size They Belong To.
