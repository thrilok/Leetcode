class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        #Bruteforce approach
        matrix = []
        for x in range(0,n):
            matrix.append([])
            for y in range(0, m):
                matrix[x].append(0)
        length_to_modified = len(indices)
        for x in range(0, length_to_modified):
            row_to_be_edited = indices[x][0]
            col_to_be_edited = indices[x][1]
            for i in range(0, m):
                matrix[row_to_be_edited][i] += 1
            for i in range(0, n):
                matrix[i][col_to_be_edited] += 1
        count = 0
        for x in range(0, n):
            for y in range(0,m):
                if matrix[x][y]%2 != 0:
                    count+=1
        return count
    
#
# Runtime: 52 ms, faster than 39.00% of Python3 online submissions for Cells with Odd Values in a Matrix.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Cells with Odd Values in a Matrix.
