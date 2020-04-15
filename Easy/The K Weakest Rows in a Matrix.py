class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dictionary = {
        
        }
        for x in range(0, len(mat)):
            temp = 0
            temp =  temp+ sum(mat[x])
            dictionary[x] = temp
        dictionary = {key: value for key, value in sorted(dictionary.items(), key=lambda item: item[1])}
        return (list(dictionary)[0:k])

# Runtime: 116 ms, faster than 45.62% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for The K Weakest Rows in a Matrix.
