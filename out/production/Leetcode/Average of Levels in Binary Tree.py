# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
            result.append(sum(level)/len(level))
        return result

# Runtime: 48 ms, faster than 86.62% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Average of Levels in Binary Tree.
