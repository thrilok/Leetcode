class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        initial_even_sum = 0
        length = len(A)
        for x in range(0, length):
            temp = A[x]
            if temp %2 ==0:
                initial_even_sum += temp
        query_length = len(queries)
        result = []
        for x in range(0, query_length):
            index = queries[x][1]
            previous = A[index]
            if previous %2 ==0:
                initial_even_sum -= previous
            next_num = queries[x][0]
            changed = next_num+previous
            if changed %2 ==0:
                initial_even_sum += changed
            A[index] = changed
            result.append(initial_even_sum)
        return result
    
# Runtime: 552 ms, faster than 87.57% of Python3 online submissions for Sum of Even Numbers After Queries.
# Memory Usage: 18.7 MB, less than 5.88% of Python3 online submissions for Sum of Even Numbers After Queries.
