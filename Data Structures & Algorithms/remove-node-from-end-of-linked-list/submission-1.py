# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [0, 1, 2, 3, 4, 5, 6, 7] n = 3

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        rab = dummy 

        while n > 0 and rab:
            n -= 1
            rab = rab.next
        
        t = dummy
        while rab and rab.next:
            rab = rab.next
            t = t.next
        
        # At this point slow points previous node of target
        temp = t.next
        t.next = temp.next
        temp.next = None
        
        return dummy.next