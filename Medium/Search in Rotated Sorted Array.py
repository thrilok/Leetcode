class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        min_nums = min(nums)
        min_index = nums.index(min_nums)
        if self.binarySearch(nums[min_index:] + nums[:min_index], target):
            return nums.index(target)
        return -1
    
    def binarySearch(self, givenList, search):
        length = len(givenList)
        left = 0
        right = length-1
        while right >= left:
            mid = (left+right)//2
            if search == givenList[mid]:
                return True
            elif search < givenList[mid]:
                right = mid-1
            else:
                left = mid+1
        return False
        
# Runtime: 40 ms, faster than 62.25% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.6 MB, less than 9.99% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        min_nums = min(nums)
        min_index = nums.index(min_nums)
        if target<= nums[len(nums)-1] and target>= min_nums:
            result = self.binarySearch(nums[min_index:], target)
        else:
            result = self.binarySearch(nums[:min_index], target)
        if result:
            return nums.index(target)
        return -1
    
    def binarySearch(self, givenList, search):
        length = len(givenList)
        left = 0
        right = length-1
        while right >= left:
            mid = (left+right)//2
            if search == givenList[mid]:
                return True
            elif search < givenList[mid]:
                right = mid-1
            else:
                left = mid+1
        return False
        
# Runtime: 36 ms, faster than 85.78% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.7 MB, less than 9.99% of Python3 online submissions for Search in Rotated Sorted Array.
