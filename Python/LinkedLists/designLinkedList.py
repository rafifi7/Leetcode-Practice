class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)

        # check if head exists
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        if self.tail is None:
            self.tail = newNode
            self.head = newNode
        else:   
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        
        # check if size is valid
        if index < 0 or index > self.size:
            return
        # if we are essentially adding to head
        if index == 0:
            self.addAtHead(val)
        # if we are essentially adding to tail
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            # create new ptr to curr's prev
            prevCurr = curr.prev
            # create new node
            newNode = Node(val)
            # point prev's next ptr to the new node
            prevCurr.next = newNode
            # point new nodes ptr to curr
            newNode.next = curr
            # point new node's ptr to curr's prev
            newNode.prev = prevCurr
            # point curr's prev ptr to new node
            curr.prev = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # check if index valid
        if index < 0 or index >= self.size or self.size == 0:
            return

        # if size == 1 and index valid
        if self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            # create new ptr for second element
            headNext = self.head.next
            # detach old head's next ptr
            self.head.next = None
            # detach new head's prev ptr
            headNext.prev = None
            # set new head to second
            self.head = headNext
        elif index == self.size - 1:
            # create ptr for second to last element
            tailPrev = self.tail.prev
            # detach new tail's next ptr
            tailPrev.next = None
            # detach old tail's prev ptr
            self.tail.prev = None
            # set tail to new tail
            self.tail = tailPrev
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            # so we are now at the correct index
            prevCurr = curr.prev
            nextCurr = curr.next
            prevCurr.next = nextCurr
            nextCurr.prev = prevCurr
            # disconnect
            curr.prev = None
            curr.next = None

        self.size -= 1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)