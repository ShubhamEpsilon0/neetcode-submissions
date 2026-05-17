# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        nh = newHead
        h1 = l1
        h2 = l2
        carry = 0
        while h1 or h2:
            if h1 and h2:
                nh.next = ListNode((h1.val + h2.val + carry) % 10)
                carry = (h1.val + h2.val + carry) // 10
                h1 = h1.next
                h2 = h2.next
            elif h1:
                nh.next = ListNode((h1.val + carry) % 10)
                carry = (h1.val + carry) // 10
                h1 = h1.next
            else:
                nh.next = ListNode((h2.val + carry) % 10)
                carry = (h2.val + carry) // 10
                h2 = h2.next

            nh = nh.next
        if carry:
            nh.next = ListNode(carry)

        return newHead.next               


        