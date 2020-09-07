class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for x in range(0, n):
            nums.append(start + 2*x)
        result = 0
        for x in nums:
            result = result ^ x
        return result

# Runtime: 24 ms, faster than 95.33% of Python3 online submissions for XOR Operation in an Array.
# Memory Usage: 13.9 MB, less than 29.96% of Python3 online submissions for XOR Operation in an Array.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for x in range(0, n):
            result = result ^ (start + 2*x)
        return result

# Runtime: 36 ms, faster than 41.45% of Python3 online submissions for XOR Operation in an Array.
# Memory Usage: 13.8 MB, less than 55.77% of Python3 online submissions for XOR Operation in an Array.
