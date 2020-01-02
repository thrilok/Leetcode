class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_table ={
        
        }
        length = len(nums)
        for x in range(0, length):
            if nums[x]>0:
                hash_table[nums[x]]= True
        hash_length = len(hash_table)
        positive = 1
        while True:
            try:
                hash_table.pop(positive)
            except:
                return positive
            positive +=1
    
# Runtime: 36 ms, faster than 70.51% of Python3 online submissions for First Missing Positive.
# Memory Usage: 13.9 MB, less than  of Python3 online submissions for First Missing Positive.
