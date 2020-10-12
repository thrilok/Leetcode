class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = a^b
        carry = a&b
        if carry ==0 :
	        return result
	return sum((carry<<1, result))

# Runtime: 24 ms, faster than 88.70% of Python3 online submissions for Sum of Two Integers.
# Memory Usage: 14 MB, less than 5.88% of Python3 online submissions for Sum of Two Integers.

print(Solution.getSum(5, 6, 6))
