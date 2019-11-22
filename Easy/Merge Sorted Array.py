class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while j<n and i<(m+j):
            if nums2[j]<nums1[i]:
                temp = m+j-1
                while temp >=i:
                    nums1[temp+1] = nums1[temp]
                    temp -=1
                nums1[i] = nums2[j]
                j +=1
            i +=1
        if j != n:
            while j<n:
                nums1[i] = nums2[j]
                i +=1
                j +=1

# Runtime: 36 ms, faster than 97.87% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
