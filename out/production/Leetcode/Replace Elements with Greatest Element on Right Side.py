class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        current_max = -1
        for x in range(length-1, -1, -1):
            temp = arr[x]
            arr[x] = current_max
            if temp > current_max:
                current_max = temp
        return arr

# Runtime: 128 ms, faster than 32.01% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
