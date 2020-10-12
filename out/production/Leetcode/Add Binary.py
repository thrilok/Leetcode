class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a_list = self.reverse(list(a))
        b_list = self.reverse(list(b))
        a_len = len(a)
        b_len = len(b)
        count = 0
        result = []
        while True:
            if count<a_len and count<b_len:
                temp = int(a_list[count])+ int(b_list[count])+ carry
                x, y = self.bin_sum(temp)
                result.append(str(x))
                carry = y
            else:
                break
            count+=1
        while count<b_len:
            temp = int(b_list[count])+ carry
            x, y = self.bin_sum(temp)
            result.append(str(x))
            carry = y
            count +=1
        while count<a_len:
            temp = int(a_list[count])+ carry
            x, y = self.bin_sum(temp)
            result.append(str(x))
            carry = y
            count +=1
        if carry ==1:
            result.append(str(carry))
        final = ''.join(self.reverse(result))
        return final
    def reverse(self, x: list) -> list :
        length = len(x)
        pt1 = 0
        pt2 = length
        while pt1<pt2:
            temp = x[pt1]
            x[pt1] = x[pt2-1]
            x[pt2-1] = temp
            pt1+=1
            pt2-=1
        return x
    def bin_sum(self, temp):
        if temp == 0:
            return (temp, 0)
        elif temp == 1:
            return(temp, 0)
        elif temp == 2:
            return (0, 1)
        elif temp ==3:
            return(1, 1)

# Runtime: 36 ms, faster than 59.42% of Python3 online submissions for Add Binary.
# Memory Usage: 14.1 MB, less than 5.29% of Python3 online submissions for Add Binary.
