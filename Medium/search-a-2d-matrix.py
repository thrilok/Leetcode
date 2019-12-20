class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		rows = len(matrix)
		if rows == 0:
			return False
		col = len(matrix[0])
		if col == 0:
			return False
		current = 0
		while current < rows:
			if matrix[current][col - 1] >= target:
				break
			current += 1
		element = 0
		if current == rows:
			return False
		while element < col:
			if matrix[current][element] == target:
				return True
			element += 1
		return False

# Runtime: 64 ms, faster than 95.54% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.8 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        col = len(matrix[0])
        for x in range(0, rows):
            for y in range(0, col):
                if matrix[x][y]==target:
                    return True
        return False
    
    
# Runtime: 88 ms, faster than 7.99% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.9 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.
