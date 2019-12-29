class Solution:
    def addDigits(self, num: int) -> int:
        number = self.digits(num)
        temp1 = sum(number)
        if temp1>=10:
            return self.addDigits(temp1)
        else:
            return temp1
    def digits(self, n):
        digits = []
        while n>0:
            temp = n%10
            digits.append(temp)
            n = int(n/10)
        return digits

# Runtime: 24 ms, faster than 96.92% of Python3 online submissions for Add Digits.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Digits.
