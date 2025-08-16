class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
       self.head = None
       self.tail = None
        

    def get(self, index: int) -> int:
        count = 0
        curr = self.head
        while curr != None and count < index:
            curr = curr.next
            count += 1
        
        return curr.val if curr else -1
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if index == 0:
            self.addAtHead(val)
        else:
            count = 0
            curr = self.head
            while curr != None and count + 1 < index:
                curr = curr.next
                count += 1

            if curr != None:
                new_node.next = curr.next
                curr.next = new_node
            if curr == self.tail:
                self.tail = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head != None:
            self.head = self.head.next
        else:
            count = 0
            curr = self.head
            while curr and count + 1 < index:
                curr = curr.next
                count += 1
            
            if curr != None and curr.next == self.tail:
                self.tail = curr
            if curr != None and curr.next != None:
                curr.next = curr.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)