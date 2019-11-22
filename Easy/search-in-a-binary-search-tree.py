class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root
        notfound = False
        while notfound == False:
            if current.val > val:
                if current.left is not None:
                    current = current.left
                else:
                    pass
            if current.val < val:
                if current.right is not None:
                    current = current.right
                else:
                    pass
            if current.val == val:
                notfound = True
                return current
        return None
