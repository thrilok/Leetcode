class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        current = left
        result = []
        while current<=right:
            temp = current
            reminder = current%10
            correct = False
            while current >0:
                if current%10==0:
                    correct = True
                    break
                if temp%reminder == 0:
                    current = int(current/10)
                    reminder = current%10
                else:
                    correct = True
                    break
            if correct!=True:
                result.append(temp)
            current = temp+1
        return result
    
    
# Runtime: 48 ms, faster than 94.76% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 13.7 MB, less than 8.00% of Python3 online submissions for Self Dividing Numbers.
