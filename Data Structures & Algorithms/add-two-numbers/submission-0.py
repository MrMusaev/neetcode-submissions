# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        extra = 0

        while l1 and l2:
            sum = l1.val + l2.val + extra
            extra = 1 if sum >= 10 else 0
            cur.next = ListNode(sum % 10)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        
        while l1:
            sum = l1.val + extra
            extra = 1 if sum >= 10 else 0
            cur.next = ListNode(sum % 10)
            l1 = l1.next
            cur = cur.next
        
        while l2:
            sum = l2.val + extra
            extra = 1 if sum >= 10 else 0
            cur.next = ListNode(sum % 10)
            l2 = l2.next
            cur = cur.next
        
        if extra:
            cur.next = ListNode(extra)
        
        return dummy.next