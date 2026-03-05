class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        idx = 0
        curr = self.head
        
        while curr and idx != index:
            curr = curr.next
            idx += 1

        if not curr:
            return -1
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        new = Node(val)
        if self.head:
            new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        curr = self.head

        if not curr:
            self.head = new
        else:
            while curr and curr.next:
                curr = curr.next
            
            curr.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            new = Node(val)
            idx = 1

            curr = self.head

            while curr and idx != index:
                curr = curr.next
                idx += 1
            
            if curr:
                temp = curr.next
                curr.next = new
                new.next = temp

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            pass
        elif index == 0:
            self.head = self.head.next
        else:
            idx = 1
            
            curr = self.head
            
            while curr and idx != index:
                curr = curr.next
                idx += 1

            if curr and curr.next:
                curr.next = curr.next.next
 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)