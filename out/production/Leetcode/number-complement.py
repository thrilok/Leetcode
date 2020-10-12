class Solution:
    def findComplement(self, num: int) -> int:
        binary = format(num, 'b')
        binary = binary.replace('1','a')
        binary = binary.replace('0','1')
        binary = binary.replace('a','0')
        return (int(binary, 2))
        
        
# Runtime: 36 ms, faster than 69.53% of Python3 online submissions for Number Complement.
# Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Number Complement.


class Solution:
    def findComplement(self, num: int) -> int:
        binary = format(num, 'b')
        binary_list = list(binary)
        bits = len(binary_list)
        for x in range(0, bits):
            if binary_list[x] =='1':
                binary_list[x] =0
            else:
                binary_list[x] =1
        binary = ''.join(str(x) for x in binary_list)
        print(binary)
        return (int(binary, 2))
        
        
# Runtime: 36 ms, faster than 69.53% of Python3 online submissions for Number Complement.
# Memory Usage: 14 MB, less than 10.00% of Python3 online submissions for Number Complement.


class Solution:
    def findComplement(self, num: int) -> int:
        binary = format(num, 'b')
        binary_list = list(binary)
        bits = len(binary_list)
        for x in range(0, bits):
            if binary_list[x] =='1':
                binary_list[x] ='0'
            else:
                binary_list[x] ='1'
        binary = ''.join(binary_list)
        return (int(binary, 2))


# Runtime: 28 ms, faster than 98.49% of Python3 online submissions for Number Complement.
# Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Number Complement.
