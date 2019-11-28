"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        current = head
        while current is not None:
            temp = Node(current.val, current.next, None)
            current.next = temp
            current = temp.next 
        if head is None:
            return current
        point1 = head
        point2 = head.next 
        
        while point1 is not None:
            if point1.random is None:
                point2.random = None
            else:
                point2.random = point1.random.next 
            if point2.next is None: 
                break 
            point1 = point2.next 
            point2 = point1.next 
        
        point1 = head
        modified_list_head = head.next
        point2 = head.next
        while point2 is not None: 
            point1.next = point2.next 
            point1 = point1.next 
            if point1 is None: 
                point2.next = None
                break
            point2.next = point1.next 
            if point2 is not None:
                point2 = point2.next
        return (modified_list_head)


# solution with two pointers
# Runtime: 32 ms, faster than 99.10% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.


    
