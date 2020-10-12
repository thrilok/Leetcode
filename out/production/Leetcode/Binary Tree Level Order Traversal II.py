# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        queue = []
        queue.append(root)
        result = []
        while queue :
            count = len(queue)
            level = []
            while count > 0:
                temp = queue.pop(0)
                level.append(temp.val)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
                count-=1
            result.append(level)
        result = result [::-1]
        return result
    
# Runtime: 32 ms, faster than 87.72% of Python3 online submissions for Binary Tree Level Order Traversal II.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal II.
