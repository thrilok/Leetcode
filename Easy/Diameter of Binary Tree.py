# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        return max(lheight+rheight, max(ldiameter, rdiameter))
        
    def height(self, root: TreeNode):
        if root == None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            ldepth = self.height(root.left)
            rdepth = self.height(root.right)
        if ldepth>rdepth:
            return ldepth+1
        else:
            return rdepth+1
