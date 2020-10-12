# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current1 = l1
        current2 = l2
        if current1 is None:
            return current2
        elif current2 is None:
            return current1
        head = None
        current = None
        while current1 is not None and current2 is not None:
            if head is None:
                if current1.val <= current2.val:
                    head = ListNode(current1.val)
                    current1 = current1.next
                else:
                    head = ListNode(current2.val)
                    current2 = current2.next
                current = head
            else:
                if current1.val <= current2.val:
                    current.next = ListNode(current1.val)
                    current1 = current1.next
                else:
                    current.next = ListNode(current2.val)
                    current2 = current2.next
                current = current.next
        if current2 is not None:
            current.next = current2
        if current1 is not None:
            current.next = current1
        return head

# Runtime: 32 ms, faster than 96.54% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

