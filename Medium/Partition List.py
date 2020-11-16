# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None or head.next == None:
            return head
        current = head
        gre_head = None
        less_head = None
        gre_tail = None
        less_tail = None
        while current != None:
            if current.val < x:
                if less_head == None:
                    less_head = current
                    less_tail = current
                else:
                    less_tail.next = current
                    less_tail = current
            else:
                if gre_head == None:
                    gre_head = current
                    gre_tail = current
                else:
                    gre_tail.next = current
                    gre_tail= current
            current = current.next
        if less_tail != None:
            less_tail.next = gre_head
        else:
            return gre_head
        if gre_tail != None:
            gre_tail.next = None
        return less_head
        
# Runtime: 36 ms, faster than 54.91% of Python3 online submissions for Partition List.
# Memory Usage: 14.1 MB, less than 32.15% of Python3 online submissions for Partition List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None or head.next == None:
            return head
        current = head
        gre_head = gre_tail = ListNode(-1)
        less_head= less_tail = ListNode(-1)
        while current != None:
            if current.val < x:
                less_tail.next = current
                less_tail = current
            else:
                gre_tail.next = current
                gre_tail= current
            current = current.next
        less_tail.next = gre_head.next
        gre_tail.next = None
        return less_head.next
        
# Runtime: 36 ms, faster than 54.91% of Python3 online submissions for Partition List.
# Memory Usage: 14.2 MB, less than 32.15% of Python3 online submissions for Partition List.
