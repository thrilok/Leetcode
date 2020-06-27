# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_l1 = l1
        current_l2 = l2
        carry = 0
        head = result = ListNode(-1)
        while current_l1 != None and current_l2 != None:
            temp = current_l1.val+ current_l2.val +carry
            if temp>9:
                carry = temp //10
            else:
                carry = 0
            result.next = ListNode(temp%10)
            result = result.next
            current_l1 = current_l1.next
            current_l2 = current_l2.next
        while current_l1 == None and current_l2 != None:
            temp = current_l2.val + carry
            if temp >9:
                carry = temp//10
            else:
                carry = 0
            result.next = ListNode(temp%10)
            result = result.next
            current_l2 = current_l2.next
        while current_l1 != None and current_l2 == None:
            temp = current_l1.val + carry
            if temp >9:
                carry = temp//10
            else:
                carry = 0
            result.next = ListNode(temp%10)
            result = result.next
            current_l1 = current_l1.next
        if carry >0:
            result.next = ListNode(carry)
        return head.next
    
# Runtime: 64 ms, faster than 94.54% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.

