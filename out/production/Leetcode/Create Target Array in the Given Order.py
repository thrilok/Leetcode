class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        count = 0
        for x in index:
            target = target[:x]+ [nums[count]] + target[x:]
            count+=1
        return target

# Runtime: 28 ms, faster than 89.79% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        count = 0
        for x in index:
            target.insert(x, nums[count])
            count+=1
        return target
    
# Runtime: 32 ms, faster than 69.43% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.
