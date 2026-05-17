# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return None

        if not head.next.next:
            if n == 1:
                head.next = None
                return head 
            else:
                return head.next
    
        frontPtr = head
        backPtr = head

        while frontPtr and n > 0:
            frontPtr = frontPtr.next
            n -= 1

        if not frontPtr:
            return head.next

        while frontPtr and frontPtr.next:
            frontPtr = frontPtr.next
            backPtr = backPtr.next

        backPtr.next = backPtr.next.next

        return head


        