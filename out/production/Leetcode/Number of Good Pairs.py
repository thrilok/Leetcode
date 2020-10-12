import collections
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x = dict(collections.Counter(nums))
        result = 0
        for key, value in x.items():
            if x[key]>1:
                temp = x[key]
                result += ((temp)*(temp-1))/2
        return int(result)

# Runtime: 44 ms, faster than 56.78% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.

import collections
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x = dict(collections.Counter(nums))
        result = 0
        for value in x.values():
            if value>1:
                result += ((value)*(value-1))/2
        return int(result)
    
# Runtime: 24 ms, faster than 99.21% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
