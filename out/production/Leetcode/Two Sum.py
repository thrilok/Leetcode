class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for x in range(0, length-1):
            for y in range(x+1, length):
                if nums[x]+nums[y]== target:
                    return (x,y)
                    
# Runtime: 6260 ms, faster than 5.08% of Python3 online submissions for Two Sum.
# Memory Usage: 13.7 MB, less than 88.37% of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        table = {
        
        }
        for x in range(0, length):
            table[nums[x]] = x
        for x in range(0, length):
            need = target - nums[x]
            try:
                temp = table[need]
                if x != temp:
                    return(x, temp)
            except:
                pass
                
# Runtime: 52 ms, faster than 79.56% of Python3 online submissions for Two Sum.
# Memory Usage: 14.4 MB, less than 34.18% of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        table = {
        
        }
        for x in range(0, length):
            need = target - nums[x]
            try:
                temp = table[need]
                if x != temp:
                    return(x, temp)
            except:
                table[nums[x]] = x
                
# Runtime: 44 ms, faster than 96.67% of Python3 online submissions for Two Sum.
# Memory Usage: 14.1 MB, less than 65.35% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {
        
        }
        for x in range(0, len(nums)):
            if target-nums[x] in hash_map:
                return [x, hash_map[target-numss[x]]]
            else:
                hash_map[nums[x]] = x

# Runtime: 52 ms, faster than 57.06% of Python3 online submissions for Two Sum.
# Memory Usage: 15.5 MB, less than 5.11% of Python3 online submissions for Two Sum.
