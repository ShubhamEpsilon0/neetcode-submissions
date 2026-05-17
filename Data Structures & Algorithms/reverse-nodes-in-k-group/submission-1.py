# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ansList = tail = ListNode()
        remList = head
        while True:
            head = remList
            remList, isFullGroup = self.returnNextGroup(remList, k)

            if not isFullGroup:
                break
            tailAfterReverse = head
            head = self.reverse(head)
            tail.next = head
            tail = tailAfterReverse

        tail.next = head
        return ansList.next

        

    def returnNextGroup (self, head, groupSize):
        if not head:
            return None, False
        temp = head
        for i in range(groupSize - 1):
            temp = temp.next
            if not temp:
                return None, False
            
        remainingList = temp.next
        temp.next = None
        return remainingList, True

    def reverse(self, head):
        if not head:
            return None
        newHead = head
        head = head.next
        newHead.next = None

        while head:
            temp = head
            head = head.next

            temp.next = newHead
            newHead = temp

        return newHead
        