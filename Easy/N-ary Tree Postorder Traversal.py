"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
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
                temp = current.children[::-1]+temp
        return result[::-1]
        
# Runtime: 44 ms, faster than 96.54% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 15.8 MB, less than 96.02% of Python3 online submissions for N-ary Tree Postorder Traversal.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root ==None:
            return result
        temp = [root]
        while len(temp)>0:
            current = temp.pop()
            if current!= None:
                result.append(current.val)
            if len(current.children) >0:
                temp = temp +current.children
        return result[::-1]
        
# Runtime: 52 ms, faster than 68.68% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 15.8 MB, less than 96.02% of Python3 online submissions for N-ary Tree Postorder Traversal.
