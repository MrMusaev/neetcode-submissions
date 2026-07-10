# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        current = head

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_head = self.reverseList(slow.next)
        slow.next = None
        new_head = ListNode(0)
        cur = new_head

        i = 0
        while head and second_head:
            if i % 2 == 0:
                cur.next = head
                head = head.next
            else:
                cur.next = second_head
                second_head = second_head.next
            cur = cur.next
            i += 1
        
        if head:
            cur.next = head
        
        head = new_head.next
