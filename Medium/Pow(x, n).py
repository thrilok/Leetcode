class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
    
# Runtime: 16 ms, faster than 99.80% of Python3 online submissions for Pow(x, n).
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pow(x, n).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        if n == -1:
            return (1/n)
        temp = self.myPow(x, n//2)
        if n%2==0:
            return temp * temp
        else:
            return x * temp * temp
