"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        if root ==None:
            return result
        temp = [root]
        while len(temp)>0:
            current = temp[0]
            if current!= None:
                result.append(current.val)
            temp.pop(0)
            if len(current.children) >0:
                temp = current.children+temp
        return result

# Runtime: 56 ms, faster than 40.30% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 15.9 MB, less than 96.20% of Python3 online submissions for N-ary Tree Preorder Traversal.
