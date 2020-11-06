class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = ''
        started = False
        for x in s:
            if x == ' ':
                if started == True:
                    break
                pass
            elif (x == '-' or x == '+') and sign == '' and started == False:
                sign = x
                started = True
            elif ord('9')>=ord(x)>=ord('0'):
                result = (10*result) + int(x)
                started = True
            else:
                break
        if result >= 2**31:
            if sign == '-':
                result = (2**31)
            else:
                result = (2**31)-1
        if sign == '-':
            return (-result)
        return result
    
# Runtime: 28 ms, faster than 93.06% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for String to Integer (atoi).
