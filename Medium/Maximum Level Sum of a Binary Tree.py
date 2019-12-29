# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
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
            result.append(sum(level))
        return result.index(max(result))+1
    
# Runtime: 340 ms, faster than 53.90% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 17.2 MB, less than 100.00% of Python3 online submissions for Maximum Level Sum of a Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return
        queue = []
        queue.append(root)
        max_sum = 0
        level_count = 0
        final = 0
        while queue :
            count = len(queue)
            level = []
            level_count +=1
            while count > 0:
                temp = queue.pop(0)
                level.append(temp.val)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
                count-=1
            level_sum = sum(level)
            if level_sum > max_sum :
                max_sum = level_sum
                final = level_count
        return final
    
# Runtime: 336 ms, faster than 57.34% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 17.3 MB, less than 100.00% of Python3 online submissions for Maximum Level Sum of a Binary Tree.

