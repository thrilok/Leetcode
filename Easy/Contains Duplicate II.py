class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {
            
        }
        for x in range(len(nums)):
            if nums[x] in hashmap:
                distance = x - hashmap[nums[x]] 
                if distance <= k:
                    return True
                else:
                    hashmap[nums[x]] = x
            else:
                hashmap[nums[x]] = x
        return False
        
# Runtime: 84 ms, faster than 91.87% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 21.7 MB, less than 7.78% of Python3 online submissions for Contains Duplicate II.
