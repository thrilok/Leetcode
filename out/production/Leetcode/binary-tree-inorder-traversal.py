# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        current = root
        stack = []
        result = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                result.append(current.val)
                current = current.right
            else:
                return result
            
            
# Iterative
# Runtime: 52 ms, faster than 5.82% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.8 MB, less than 6.56% of Python3 online submissions for Binary Tree Inorder Traversal.


