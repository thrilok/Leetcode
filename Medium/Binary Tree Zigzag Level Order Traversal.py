# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        queue1 = []
        queue2 = []
        queue1.append(root)
        result = []
        while len(queue1) != 0 or len(queue2) != 0:
            level1 = []
            while (not len(queue1) == 0):
                temp = queue1[-1]
                queue1.pop()
                level1.append(temp.val)
                if temp.left is not None:
                    queue2.append(temp.left)
                if temp.right is not None:
                    queue2.append(temp.right)
            if len(level1) !=0:
                result.append(level1)
            level2 = []
            while (not len(queue2) == 0):
                temp = queue2[-1]
                queue2.pop()
                level2.append(temp.val)
                if temp.right is not None:
                    queue1.append(temp.right)
                if temp.left is not None:
                    queue1.append(temp.left)
            if len(level2) != 0:
                result.append(level2)
        return result

# Runtime: 28 ms, faster than 92.26% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

