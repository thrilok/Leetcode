# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root
        

# Runtime: 36 ms, faster than 74.88% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.8 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.


        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        if root.left is None and root.right is None:
            return root
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root


# Runtime: 36 ms, faster than 74.88% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.7 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.
