# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val
        current = root
        stack = []
        while True:
            if current is not None:
                if current.val != value:
                    return False
                stack.append(current)
                current = current.left
            elif (stack):
                current = stack.pop()
                current = current.right
            else:
                break
        return True
    
    
# Runtime: 36 ms, faster than 79.76% of Python3 online submissions for Univalued Binary Tree.
# Memory Usage: 13.7 MB, less than 7.69% of Python3 online submissions for Univalued Binary Tree.
