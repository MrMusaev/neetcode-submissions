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

        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        i = 0

        while fast:
            if i > n:
                slow = slow.next
            fast = fast.next            
            i += 1
        
        # At this point slow points previous node of target
        removing = slow.next
        slow.next = slow.next.next
        removing.next = None
        
        return dummy.next