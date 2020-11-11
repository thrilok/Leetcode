# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0
        n2 = 0
        current = l1
        while current != None:
            n1 = current.val + n1*10
            current = current.next
        current = l2
        while current != None:
            n2 = current.val + n2*10
            current = current.next
        total = n1+n2
        temp = []
        result = None
        while total > 0:
            temp.append(total %10)
            total = total //10
        temp = temp[::-1]
        for x in temp:
            if result == None:
                result = ListNode(x)
                current = result
            else:
                current.next = ListNode(x)
                current = current.next
        if result == None:
            return ListNode(0)
        return result
    
# Runtime: 60 ms, faster than 99.09% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        current = l1
        while current != None:
            s1.append(current.val)
            current = current.next
        current = l2
        while current != None:
            s2.append(current.val)
            current = current.next
        carry =0
        result = []
        while len(s2) >0 and len(s1)>0:
            temp = s1.pop() + s2.pop() +carry
            result.append(temp %10)
            carry = temp//10
        while len(s1) ==0 and len(s2)>0:
            temp = s2.pop() + carry
            result.append(temp %10)
            carry = temp//10
        while len(s2) ==0 and len(s1) >0:
            temp = s1.pop() + carry
            result.append(temp %10)
            carry = temp//10
        if carry !=0:
            result.append(carry)
        result.reverse()
        answer = ListNode(-1)
        current = answer
        for x in result:
            current.next = ListNode(x)
            current = current.next
        return answer.next
    
# Runtime: 80 ms, faster than 27.56% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        current = l1
        while current != None:
            s1.append(current.val)
            current = current.next
        current = l2
        while current != None:
            s2.append(current.val)
            current = current.next
        newsum =0
        result = ListNode()
        len1 = len(s1)
        len2 = len(s2)
        while len1 >0 or len2>0:
            if len1 >0:
                newsum +=s1.pop()
                len1 -=1
            if len2 >0:
                newsum +=s2.pop()
                len2-=1
            result.val = newsum%10
            newsum = newsum//10
            head = ListNode(newsum)
            head.next = result
            result = head
        if newsum ==0:
            return result.next
        return result

# Runtime: 68 ms, faster than 88.27% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.
