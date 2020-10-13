class Solution:
    def maxDepth(self, s: str) -> int:
        open_para = 0
        max_depth = 0
        for x in s:
            if x =='(':
                open_para +=1
                if open_para > max_depth:
                    max_depth = open_para
            elif x == ')':
                open_para -=1
            else:
                pass
        if open_para ==0:
            return max_depth
        return -1
 
# Runtime: 28 ms, faster than 91.77% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
