class Solution:
    def multiply(
        elf, num1: str, num2: str) -> str:
        result = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        count = 0
        for x in num1:
            temp = ''
            carry = 0
            for y in num2:
                mul = int(x)*int(y)
                add = mul + carry
                carry = 0
                num = (add%10)
                if add > 9:
                    carry = add//10
                temp =  str(num) + temp
            temp =  str(carry) + temp + '0'*count
            count += 1
            result = result + int(temp)
        return str(result)
    
# Runtime: 216 ms, faster than 14.69% of Python3 online submissions for Multiply Strings.
# Memory Usage: 13.6 MB, less than 7.14% of Python3 online submissions for Multiply Strings.

