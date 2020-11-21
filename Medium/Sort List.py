# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        givenList = []
        current = head
        while current != None:
            givenList.append(current)
            current = current.next
        sortedList = self.mergeSort(givenList)
        length = len(sortedList)
        for x in range(length-1):
            sortedList[x].next = sortedList[x+1]
        return sortedList[0]
    
    def merge(self, list1, list2):
        len1 = len(list1)
        len2 = len(list2)
        x = y = 0
        mergedList = []
        while x <len1 and y<len2:
            if list1[x].val <list2[y].val:
                mergedList.append(list1[x])
                x+=1
            elif list1[x].val >list2[y].val:
                mergedList.append(list2[y])
                y+=1
            else:
                mergedList.append(list1[x])
                mergedList.append(list2[y])
                x+=1
                y+=1
        if x == len1 and y<len2:
            while y <len2:
                mergedList.append(list2[y])
                y+=1
        if y == len2 and x<len1:
            while x <len1:
                mergedList.append(list1[x])
                x+=1
        return mergedList
    
    def mergeSort(self, arrayToSort):
        if len(arrayToSort) ==0:
            return
        if len(arrayToSort) == 1:
            arrayToSort[0].next = None
            return arrayToSort
        sortedList1 = self.mergeSort(arrayToSort[:len(arrayToSort)//2])
        sortedList2 = self.mergeSort(arrayToSort[len(arrayToSort)//2:])
        mergedList = self.merge(sortedList1, sortedList2)
        return mergedList

# Runtime: 564 ms, faster than 5.48% of Python3 online submissions for Sort List.
# Memory Usage: 31.7 MB, less than 10.94% of Python3 online submissions for Sort List.
