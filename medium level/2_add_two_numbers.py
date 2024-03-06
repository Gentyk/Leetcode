# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        plus = 0
        a = l1.val
        b = l2.val
        n = (a+b+plus) % 10
        new = ListNode(val=n)
        plus = (a+b+plus)//10
        head = new
        while l1.next or l2.next or plus:
            a = 0
            if l1.next:
                l1 = l1.next
                a = l1.val
            b = 0
            if l2.next:
                l2 = l2.next
                b = l2.val
            n = (a+b+plus) % 10
            _new = ListNode(val=n)
            new.next = _new
            new = new.next
            plus = (a+b+plus)//10
        return head