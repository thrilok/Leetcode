# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        if fast == None:
            head2 = slow
        else:
            head2 = slow.next
        current2 = self.reverseSecondHalf(head2)
        current1 = head
        while current2 != None:
            if current2.val != current1.val:
                return False
            current2 = current2.next
            current1 = current1.next
        return True
        
    def reverseSecondHalf(self, head):
        current = head
        prev = None
        while current != None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev
  
# Runtime: 60 ms, faster than 96.13% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 24.2 MB, less than 40.94% of Python3 online submissions for Palindrome Linked List.
