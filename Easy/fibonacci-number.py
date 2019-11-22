class Solution:
    def fib(self, N: int) -> int:
        result = 0
        if N ==0:
            return 0
        if N==1:
            return 1
        if N>1:
            result += self.fib(N-1)+ self.fib(N-2)
        return result
    
# Runtime: 1400 ms
# Memory Usage: 13.7 MB

class Solution:
    def fib(self, N: int) -> int:
        result = [0, 1]
        temp = 2
        while temp<=N:
            result.append(result[temp-1]+result[temp-2])
            temp +=1
        return result[N]

# Runtime: 40 ms, faster than 45.41% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.


class Solution:
    def fib(self, N: int) -> int:
        result = [0, 1]
        if N<2:
            return N
        temp = 2
        while temp<=N:
            result.append(result[0]+result[1])
            result.pop(0)
            temp +=1
        return result[1]

# Runtime: 36 ms, faster than 74.62% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.7 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
