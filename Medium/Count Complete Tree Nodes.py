# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # Do a traversal and return
        if root is None:
            return 0
        level = [root]
        count = 0
        while len(level) != 0:
            current = level[0]
            if current.left:
                level.append(current.left)
            if current.right:
                level.append(current.right)
            count+=1
            level.pop(0)
        return count
        
# Runtime: 132 ms, faster than 6.80% of Python3 online submissions for Container With Most Water.
# Memory Usage: 21 MB, less than 93.12% of Python3 online submissions for Container With Most Water.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # Do a traversal and return
        left = root
        right = root
        left_count = 0
        right_count = 0
        while left is not None:
            left_count += 1
            left = left.left
        while right is not None:
            right_count +=1
            right = right.right
        if left_count == right_count:
            return (2**left_count)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
    
# Runtime: 80 ms, faster than 81.77% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21 MB, less than 93.12% of Python3 online submissions for Count Complete Tree Nodes.
