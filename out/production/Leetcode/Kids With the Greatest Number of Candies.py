class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        answer = []
        for x in candies:
            if x+extraCandies>= maximum:
                answer.append(True)
            else:
                answer.append(False)
        return answer
# Runtime: 32 ms, faster than 97.15% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Kids With the Greatest Number of Candies.

