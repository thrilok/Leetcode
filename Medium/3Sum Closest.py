class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        close = float(inf)
        result = float(inf)
        nums.sort()
        if len(nums)<3:
            return -1
        length = len(nums)
        for i in range(length-2):
            new_target = target - nums[i]
            left = i+1
            right = length-1
            while left <right:
                temp = nums[left]+nums[right]+nums[i]
                new_close = abs(temp-target)
                print(close, new_close)
                if temp >target:
                    right-=1
                elif temp < target:
                    left +=1
                else:
                    return target
                if close >new_close:
                    close = new_close
                    result = temp
        return result

# Runtime: 248 ms, faster than 31.08% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.5 MB, less than 99.97% of Python3 online submissions for 3Sum Closest.
