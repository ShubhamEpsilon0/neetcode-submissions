# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
         
        head1, head2 = self.divideList(head)
        head2 = self.reverseList(head2)
        self.mergeList(head1, head2)

    def divideList (self, head):
        fast = head
        slow = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        nextHead = slow.next
        slow.next = None
        return head, nextHead

    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head

        curNode = head
        nextNode = head.next
        curNode.next = None
        newHead = self.reverseList(nextNode)
        nextNode.next = curNode

        return newHead

    def mergeList(self, head1, head2):
        head1Ptr = head1
        head2Ptr = head2

        while head1Ptr and head2Ptr:
            temp = head1Ptr
            head1Ptr = head1Ptr.next
            temp.next = head2Ptr
            head2Ptr = head2Ptr.next
            temp.next.next = head1Ptr


        