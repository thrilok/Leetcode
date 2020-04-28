class Solution:
    def reverseBits(self, n: int) -> int:
        n_binary = bin(n)[2:]
        if len(n_binary)<32:
            n_binary = (32-len(n_binary))*'0'+n_binary
        output_string= n_binary[::-1]
        return int(output_string, 2)

# Runtime: 24 ms, faster than 94.28% of Python3 online submissions for Reverse Bits.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reverse Bits.
