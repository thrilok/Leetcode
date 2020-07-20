class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array_paths = []
        for i in range(n):
            array_paths.append([0] * m)
        for x in range(0, n):
            array_paths[x][m-1] = 1
        for x in range(0, m):
            array_paths[n-1][x] = 1
        for x in range(n-2, -1, -1):
            for y in range(m-2, -1, -1):
                array_paths[x][y] = array_paths[x+1][y] + array_paths[x][y+1]
        return array_paths[0][0]

# Runtime: 28 ms, faster than 81.01% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.7 MB, less than 93.04% of Python3 online submissions for Unique Paths.
