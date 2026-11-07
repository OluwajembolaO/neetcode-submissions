# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, head):
        prev = None
        curr = head
        while curr:
            saveStar = curr.next
            curr.next = prev
            prev = curr
            curr = saveStar
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        l, r = head, head.next
        while r and r.next:
            l = l.next
            r = r.next.next
        secondHalf = l.next
        l.next = None
        firstHalf = head
        secondHalf = self.reverseLL(secondHalf)
        
        l = firstHalf
        r = secondHalf

        while r:
            spl = l.next
            spr = r.next
            l.next = r
            r.next = spl
    
            l = spl
            r = spr

        
        