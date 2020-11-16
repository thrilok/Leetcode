# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        i = head
        j = head.next
        even_head = head.next
        while i != None and j != None and j.next != None:
            i.next = j.next
            j.next = j.next.next
            i = i.next
            j = j.next
        i.next = even_head
        return head
    
# Runtime: 36 ms, faster than 93.07% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 16 MB, less than 19.27% of Python3 online submissions for Odd Even Linked List.
