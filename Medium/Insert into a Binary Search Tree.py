# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root
        while True:
            if current.val >val:
                if current.left is None:
                    break
                current = current.left
            else:
                if current.right is None:
                    break
                current = current.right
        if current.val > val:
            current.left = TreeNode(val)
        else:
            current.right = TreeNode(val)
        return root
    

# Runtime: 112 ms, faster than 98.97% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Insert into a Binary Search Tree.
