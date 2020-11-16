# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = []
        current = head
        while current is not None:
            result.append(str(current.val))
            current = current.next
        temp = int(''.join(result), 2)
        return temp
    
# Runtime: 32 ms, faster than 27.79% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result =  0
        current = head
        while current != None:
            result = result *2 + current.val
            current = current.next
        return result
        
# Runtime: 28 ms, faster than 79.67% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# # Memory Usage: 14.1 MB, less than  of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
