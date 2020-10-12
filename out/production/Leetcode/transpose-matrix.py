class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        rows = len(A)
        columns = len(A[0])
        for col in range(0, columns):
            temp = []
            for row in range(0, rows):
                temp.append(A[row][col])
            result.append(temp)
        return result
        
    
# Runtime: 96 ms, faster than 13.85% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 14.6 MB, less than 5.72% of Python3 online submissions for Transpose Matrix.
#
# Time Complexity: O(R∗C), where RR and CC are the number of rows and columns in the given matrix A.
#
# Space Complexity: O(R∗C), the space used by the answer.
