# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        q = head
        while q != None and q.next != None:
            p = p.next
            q = q.next.next
            if p ==q:
                return True
        return False
    
# Runtime: 44 ms, faster than 91.18% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
