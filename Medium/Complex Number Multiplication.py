class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a1, a2 = a.split('+')
        b1, b2 = b.split('+')
        a1, b1 = int(a1), int(b1)
        result = str(a1*b1 + (int(a2.replace('i', '')) * int(b2.replace('i', '')) *-1))+ '+' +str(int(a2.replace('i', ''))*b1 + int(b2.replace('i', ''))*a1)+'i'
        return result

# Runtime: 32 ms, faster than 34.02% of Python3 online submissions for Complex Number Multiplication.
# Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Complex Number Multiplication.


