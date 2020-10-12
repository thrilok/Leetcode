class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        cols = len(mat[0])
        rows = len(mat)
        middle = cols//2
        result = 0
        for x in range (0, rows):
            result += (mat[x][x] +mat[x][cols-x-1])
        if rows%2 !=0:
            result = result - mat[middle][middle]
        return result

# Runtime: 100 ms, faster than 100.00% of Python3 online submissions for Matrix Diagonal Sum.
# Memory Usage: 14.1 MB, less than 33.33% of Python3 online submissions for Matrix Diagonal Sum.
