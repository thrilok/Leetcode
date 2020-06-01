class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = format(N, 'b')
        binary_list = list(binary)
        bits = len(binary_list)
        for x in range(0, bits):
            if binary_list[x] =='1':
                binary_list[x] ='0'
            else:
                binary_list[x] ='1'
        binary = ''.join(binary_list)
        return (int(binary, 2))
        
# Runtime: 28 ms, faster than 69.43% of Python3 online submissions for Complement of Base 10 Integer.
# Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Complement of Base 10 Integer.

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = format(N, 'b')
        binary_list = list(binary)
        bits = len(binary_list)
        for x in range(0, bits):
            if binary_list[x] =='1':
                binary_list[x] ='0'
            else:
                binary_list[x] ='1'
        binary = ''.join(binary_list)
        return (int(binary, 2))


# Runtime: 40 ms, faster than 30.15% of Python3 online submissions for Complement of Base 10 Integer.
# Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Complement of Base 10 Integer.

