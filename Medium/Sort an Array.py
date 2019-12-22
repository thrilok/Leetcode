## Merge Sort

class Solution:
    sorted_array = []
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)>1:
            mid = int(len(nums)/2)
            left = nums[:mid]
            right = nums[mid:]
            self.sortArray(left)
            self.sortArray(right)
            i = j = k = 0

            # merging
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i +=1
                else:
                    nums[k] = right[j]
                    j +=1
                k +=1

            # only
            while i < len(left):
                nums[k] = left[i]
                i +=1
                k +=1
            while j < len(right):
                nums[k] = right[j]
                j +=1
                k +=1
        return nums
    
# Runtime: 416 ms, faster than 23.50% of Python3 online submissions for Sort an Array.
# Memory Usage: 18.8 MB, less than 100.00% of Python3 online submissions for Sort an Array.


