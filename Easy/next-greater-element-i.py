class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        len1= len(nums1)
        for x in range(0, len1):
            item = nums1[x]
            temp = False
            found = False
            len2 = len(nums2)
            for y in range(0, len2):
                no2 = nums2[y]
                if item == no2:
                    found = True
                if found == True and item < no2:
                    result.append(no2)
                    temp = True
                    break
            if temp == False:
                result.append(-1)
        return result
    
# Runtime: 264 ms, faster than 5.18% of Python3 online submissions for Next Greater Element I.
# Memory Usage: 13.9 MB, less than 7.41% of Python3 online submissions for Next Greater Element I.
