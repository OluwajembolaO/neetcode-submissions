class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy.next
        for i in range(index):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        prev = self.dummy
        for i in range(index):
            prev = prev.next
        prev.next = ListNode(val, prev.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.dummy
        for i in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1