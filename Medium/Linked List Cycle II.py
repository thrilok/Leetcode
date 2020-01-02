	# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p = head
        q = head
        while q != None and q.next != None:
            p = p.next
            q = q.next.next
            if p ==q:
                return self.CycleStart(p, head)
        return None
    def CycleStart(self, p: ListNode, q: ListNode) -> ListNode:
        while p !=q:
            p = p.next
            q = q.next
        return p
    
# Runtime: 48 ms, faster than 85.35% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.
