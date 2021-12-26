from utility.LinkedListNode import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self.dummyHead = LinkedListNode(0)
        self.tail = self.dummyHead
        self.head = None

    def createElement(self, key):
        if self.tail and not self.tail.next:
            currNode = LinkedListNode(key)
            self.tail.next = currNode
            currNode.prev = self.tail
            self.tail = self.tail.next
            if self.head is None:
                self.head = currNode
            return currNode

    def addElementToLast(self, node):
        if node:
            if node == self.tail:
                return
            if node == self.head:
                self.head = self.head.next
                node.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None

    def deleteNode(self):
        if self.head:
            curr = self.head
            key = curr.val
            self.head = self.head.next
            curr.next = None
            self.head.prev = None
            del curr
            return key
        return None
