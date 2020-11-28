class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        final = [[1], [1,1]]
        count = 2
        if rowIndex <2:
            return final[rowIndex]
        prev = [1, 1]
        result = []
        while count <= rowIndex:
            result = [0] * (count+1)
            for x in range(1, count):
                result[x] = prev[x]  + prev[x-1]
            result[0] = 1
            result[count] = 1
            prev = result
            count+=1
        return result

# Runtime: 28 ms, faster than 80.03% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 14.4 MB, less than 10.43% of Python3 online submissions for Pascal's Triangle II.