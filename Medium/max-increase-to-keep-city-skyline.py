class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        top = []
        left = []
        rows = len(grid)
        col = len(grid[0])
        for x in range(0, rows):
            left.append(max(grid[x]))
        for x in range(0, col):
            maximum = grid[0][x]
            for y in range(1,rows):
                if maximum < grid[y][x]:
                    maximum = grid[y][x]
            top.append(maximum)
        answer = 0
        for x in range(0, rows):
            for y in range(0, col):
                answer += (min([top[x], left[y]])- grid[x][y])
        return answer
