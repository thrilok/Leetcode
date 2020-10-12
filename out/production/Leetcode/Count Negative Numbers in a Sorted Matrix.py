class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        column = len(grid[0])
        count = 0
        for x in range(0, rows):
            for y in range(0, column):
                if grid[x][y]<0:
                    count +=1
        return count


# Runtime: 132 ms, faster than 50.56% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        column = len(grid[0])
        count = 0
        for x in range(rows-1, -1, -1):
            for y in range(column-1, -1, -1):
                if grid[x][y]<0:
                    count +=1
        return count

# Runtime: 116 ms, faster than 98.96% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.


