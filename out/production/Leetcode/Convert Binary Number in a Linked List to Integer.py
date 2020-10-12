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
