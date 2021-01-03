# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = None
        current = list1
        count = 0
        while current != None:
            if count < a:
                current = current.next
                count += 1 
                if prev == None:
                    prev = list1
                else:
                    prev = prev.next
            elif count == a:
                prev.next = list2
                secondListPtr = list2
                while count != b:
                    current = current.next
                    count+=1
                while secondListPtr.next != None:
                    secondListPtr = secondListPtr.next
                secondListPtr.next = current.next
                return list1
        return list1

# Runtime: 468 ms, faster than 36.56% of Python3 online submissions for Merge In Between Linked Lists.
# Memory Usage: 20 MB, less than 92.11% of Python3 online submissions for Merge In Between Linked Lists.