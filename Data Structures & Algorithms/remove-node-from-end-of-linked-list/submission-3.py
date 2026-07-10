class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        fast = dummy 

        while n > 0 and fast:
            n -= 1
            fast = fast.next
        
        slow = dummy
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        temp = slow.next
        slow.next = temp.next
        temp.next = None
        
        return dummy.next