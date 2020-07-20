class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {
            
        }
        if len(nums)>0:
            maximum = nums[0]
        for x in nums:
            if x in frequency:
                temp = frequency[x]+1
                frequency[x]= temp
                if temp > maximum:
                    maximum = temp
            else:
                frequency[x] = 1
        bucket = [[] for _ in range(maximum)]
        result = []
        count = k
        for key, value in frequency.items():
            bucket[value-1].append(key)
        for x in range(len(bucket)-1, -1, -1):
            if len(bucket[x])<count:
                result.extend(bucket[x][:])
                count -=len(bucket[x])
            else:
                result.extend(bucket[x][:count])
                count -=len(bucket[x][:count])
            if count ==0:
                return result

# Runtime: 108 ms, faster than 76.82% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18 MB, less than 95.63% of Python3 online submissions for Top K Frequent Elements.
