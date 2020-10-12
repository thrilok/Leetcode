class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num>0:
            if num%2 ==0:
                num = num//2
            else:
                num -=1
            count +=1
        return count
    
# Runtime: 28 ms, faster than 66.67% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

class Solution:
    def numberOfSteps (self, num: int) -> int:
        binary = bin(num)[2:]
        result = 0
        if binary[-1]=='1':
            result+=1
        for x in range(0, len(binary)-1):
            if binary[x]=='1':
                result +=2
            else:
                result +=1
        return result
    
# Runtime: 28 ms, faster than 66.67% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

