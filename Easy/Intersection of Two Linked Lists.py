# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        cur2 = headB
        len1, len2 = 1, 1
        while cur1 != None and cur1.next != None:
            cur1 = cur1.next
            len1+=1
        while cur2 != None and cur2.next != None:
            cur2 = cur2.next
            len2+=1
        if cur1 != cur2:
            return None
        change = abs(len1-len2)
        count = 0
        cur1 = headA
        cur2 = headB
        if len1> len2:
            while count < change:
                cur1 = cur1.next
                count +=1
        else:
            while count < change:
                cur2 = cur2.next
                count +=1
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
        
# Runtime: 168 ms, faster than 46.18% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 29.2 MB, less than 60.71% of Python3 online submissions for Intersection of Two Linked Lists.
