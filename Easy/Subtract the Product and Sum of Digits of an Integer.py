class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        while n>0:
            temp = n%10
            digits.append(temp)
            n = int(n/10)
        sum_digits = sum(digits)
        product = 1
        length = len(digits)
        for x in range(0, length):
            product = product * digits[x]
        return(product-sum_digits)
        
# Runtime: 28 ms, faster than 57.49% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
