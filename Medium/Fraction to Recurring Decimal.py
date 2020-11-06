class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = ''
        n = abs(numerator)
        d = abs(denominator)
        quo = n // d
        rem = n % d
        ans += str(quo)
        if rem != 0:
            ans +='.'
            reminder_hash = {
            
            }
            while rem != 0:
                if rem not in reminder_hash:
                    reminder_hash[rem] = len(ans)
                    rem *=10
                    quo = rem // d
                    rem = rem % d
                    ans += str(quo)
                else:
                    ans = ans[0:reminder_hash[rem]]+'('+ ans[reminder_hash[rem]:]+')'
                    break
        if (numerator<0 and denominator <0) or (numerator >0 and denominator>0) or numerator ==0:
            return ans
        return ('-'+ans)

# Runtime: 32 ms, faster than 53.40% of Python3 online submissions for Fraction to Recurring Decimal.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Fraction to Recurring Decimal.
