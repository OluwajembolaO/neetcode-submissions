# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def lengthLL(self, head):
        counter = 0
        while head:
            head = head.next
            counter += 1
        return counter
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        length = self.lengthLL(head)
        for i in range(length - n):
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next
        