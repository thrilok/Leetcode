class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length_of_array = len(arr)
        dictionary = {
        
        }
        for x in arr:
            if x in dictionary:
                dictionary[x] +=1
            else:
                dictionary[x] = 1
        values = sorted(dictionary.values(), reverse=True)
        count = 0
        current_length = length_of_array
        while current_length>int(length_of_array/2):
            current_length -= values[count]
            count +=1
        return count
    
# Runtime: 624 ms, faster than 78.61% of Python3 online submissions for Reduce Array Size to The Half.
# Memory Usage: 29.5 MB, less than 100.00% of Python3 online submissions for Reduce Array Size to The Half.
