class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = []
        for x in range(0, length):
            temp = 0
            for y in range(0, length):
                if x == y:
                    pass
                else:
                    if nums[x]>nums[y]:
                        temp +=1
            answer.append(temp)
        return answer
# Runtime: 548 ms, faster than 11.54% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = []
        hashmap = {}
        sortedNum = sorted(nums)
        for i in range(length):
            temp = sortedNum[i]
            if temp not in hashmap:
                hashmap[temp] = i
        for x in nums:
            answer.append(hashmap[x])
        return answer
        
# Runtime: 48 ms, faster than 96.75% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
