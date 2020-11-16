"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        self.recursiveConnect(root, root)
        return root
        
    def recursiveConnect(self, current, parent):
        if parent.left == current:
            if parent.right != None:
                current.next = parent.right
            else:
                self.findNext(current, parent)
        elif parent.right == current and parent.next != None:
            self.findNext(current, parent)
        if current.right != None:
            self.recursiveConnect(current.right, current)
        if current.left != None:
            self.recursiveConnect(current.left, current)
    
    def findNext(self, current, parent):
        finder = parent.next
        while finder != None:
            if finder.left != None:
                current.next = finder.left
                return
            elif finder.right != None:
                current.next = finder.right
                return
            else:
                finder = finder.next
        current.next = None
        return

# Runtime: 52 ms, faster than 38.87% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 15.2 MB, less than 5.65% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
