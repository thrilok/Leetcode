# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = None
        if head == None or head.next == None:
            return head
        current = head.next
        current_start = head
        duplicate = False
        while current != None:
            if current_start.val == current.val:
                duplicate = True
            else:
                if duplicate and prev != None:
                    prev.next = current
                    duplicate = False
                elif duplicate and prev == None:
                    head = current
                    duplicate = False
                else:
                    prev = current_start
                current_start = current
            current = current.next
        if duplicate and prev != None:
            prev.next = None
        elif duplicate and prev == None:
            return None
        return head
        
# Runtime: 40 ms, faster than 71.52% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 14.1 MB, less than 66.44% of Python3 online submissions for Remove Duplicates from Sorted List II.
