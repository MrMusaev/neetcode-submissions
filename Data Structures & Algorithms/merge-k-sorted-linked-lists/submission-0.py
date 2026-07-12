# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoSortedLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        while h1 and h2:
            if h1.val <= h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        
        if h1:
            cur.next = h1
        
        if h2:
            cur.next = h2
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        finalHead = lists[0]

        for i in range(1, len(lists)):
            curHead = lists[i]
            finalHead = self.mergeTwoSortedLists(finalHead, curHead)

        return finalHead  