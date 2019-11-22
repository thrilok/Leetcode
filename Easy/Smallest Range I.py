class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        minimum = min(A)
        maximum = max(A)
        average = int((minimum+maximum)/2)
        length = len(A)
        B = [0]*length
        for x in range(0, length):
            if A[x]<average:
                number = average- A[x]
                B[x] = (A[x]+K) if (number>K) else (A[x]+number)
            elif A[x]>average:
                number = A[x]-average
                B[x] = (A[x]-K) if (number>K) else (A[x]-number)
            else:
                B[x] = A[x]
        answer = max(B)-min(B)
        return answer
    

# Runtime: 144 ms, faster than 25.05% of Python3 online submissions for Smallest Range I.
# Memory Usage: 13.8 MB, less than 88.89% of Python3 online submissions for Smallest Range I.


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        minimum = min(A)
        maximum = max(A)
        average = int((minimum+maximum)/2)
        length = len(A)
        B = [0]*length
        for x in range(0, length):
            number = abs(average- A[x])
            if A[x]<average:
                B[x] = (A[x]+K) if (number>K) else (A[x]+number)
            elif A[x]>average:
                B[x] = (A[x]-K) if (number>K) else (A[x]-number)
            else:
                B[x] = A[x]
        answer = max(B)-min(B)
        return answer
    

# Runtime: 144 ms, faster than 25.05% of Python3 online submissions for Smallest Range I.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Smallest Range I.



class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        average = int((min(A)+max(A))/2)
        length = len(A)
        B = [0]*length
        for x in range(0, length):
            number = abs(average- A[x])
            if A[x]<average:
                A[x] = (A[x]+K) if (number>K) else (A[x]+number)
            elif A[x]>average:
                A[x] = (A[x]-K) if (number>K) else (A[x]-number)
        answer = max(A)-min(A)
        return answer
    
# Runtime: 136 ms, faster than 68.33% of Python3 online submissions for Smallest Range I.
# Memory Usage: 13.9 MB, less than 88.89% of Python3 online submissions for Smallest Range I.
