class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_length = len(stones)
        if stones_length ==0:
            return 0
        elif stones_length ==1:
            return stones[0]
        elif stones_length ==2:
            return abs(stones[0]-stones[1])
        else:
            max1 = min([stones[0], stones[1]])
            index_max1 = stones.index(max1)
            max2 = max([stones[0], stones[1]])
            index_max2 = stones.index(max2)
            for x in range(2, stones_length):
                if max1<stones[x]<=max2:
                    max1 = stones[x]
                    index_max1 = x
                elif max2<stones[x]:
                    max1 = max2
                    index_max1 = index_max2
                    max2 = stones[x]
                    index_max2 = x
            if max1 == max2:
                print(max1, max2)
                stones.pop(index_max1)
                stones.pop(index_max2)
            else:
                stones[index_max2] = (max2-max1)
                stones.pop(index_max1)
            return self.lastStoneWeight(stones)
        
# Runtime: 32 ms, faster than 95.96% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
