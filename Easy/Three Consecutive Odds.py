class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        result = []
        for x in arr:
            if x%2 !=0:
                result.append(x)
                if len(result) ==3:
                    return True
            else:
                result = []
        return False
    
# Runtime: 48 ms, faster than 57.03% of Python3 online submissions for Three Consecutive Odds.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Three Consecutive Odds.
