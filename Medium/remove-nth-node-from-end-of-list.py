# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        count = 0
        while count != n+1:
            fast = fast.next
            count+=1
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
    
# Runtime: 40 ms, faster than 55.02% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
