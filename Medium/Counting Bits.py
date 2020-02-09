# Naive approach

class Solution:
    def countBits(self, num: int) -> List[int]:
        i = 0
        answer = []
        while i<=num:
            in_bit = format(i, 'b')
            length = len(in_bit)
            count = 0
            for x in range(0, length):
                if in_bit[x] == '1':
                    count +=1
            answer.append(count)
            i = i+1
        return answer
    
# Runtime: 204 ms, faster than 10.48% of Python3 online submissions for Counting Bits.
# Memory Usage: 19.8 MB, less than 5.00% of Python3 online submissions for Counting Bits.

class Solution:
    def countBits(self, num: int) -> List[int]:
        i = 0
        answer = []
        while i<=num:
            no_of_bits = 0
            temp = i
            while temp!=0:
                if temp%2 ==1:
                    no_of_bits +=1
                temp = temp//2
            answer.append(no_of_bits)
            i = i+1
        return answer
    
# Runtime: 232 ms, faster than 6.82% of Python3 online submissions for Counting Bits.
# Memory Usage: 19.9 MB, less than 5.00% of Python3 online submissions for Counting Bits.

class Solution:
    def countBits(self, num: int) -> List[int]:
        power_bit = 1
        addition_bit = 0
        answer = [0]*(num+1)
        while power_bit<=num:
            while addition_bit<power_bit and addition_bit+power_bit <= num:
                answer[power_bit+addition_bit] = answer[addition_bit]+1
                addition_bit+=1
            addition_bit =0
            power_bit = 2*power_bit
            #power_bit = power_bit<<1
        return answer

# Runtime: 80 ms, faster than 85.51% of Python3 online submissions for Counting Bits.
# Memory Usage: 19.7 MB, less than 5.00% of Python3 online submissions for Counting Bits.
# https://www.programcreek.com/2015/03/leetcode-counting-bits-java/
# https://www.youtube.com/watch?v=QjEyO1137cM

