# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dN = ListNode(-1)
        temp = dN
        while list1 or list2:
            if not list2:
                temp.next = list1
                return dN.next
            elif not list1:
                temp.next = list2
                return dN.next
            elif list1.val < list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            elif list2.val < list1.val:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
            else:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
        return dN.next