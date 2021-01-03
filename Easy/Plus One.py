class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        result = digits
        carry = False
        carryDigit = 1
        for x in range(length-1, -1, -1):
            result[x] = result[x]+carryDigit
            if result[x] <10:
                carry = False
                break
            else:
                carry = True
                carryDigit = result[x]//10
                result[x] = result[x]%10
        if carry:
            result.insert(0, carryDigit)
        return result
    
# Runtime: 32 ms, faster than 63.73% of Python3 online submissions for Plus One.
# Memory Usage: 14.2 MB, less than 59.95% of Python3 online submissions for Plus One.
