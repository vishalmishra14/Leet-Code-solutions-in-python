class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, position):

        if self.head is None:
            return

        _temp = self.head

        if position == 0:
            self.head = _temp.next
            _temp = None
            return

        for i in range(position-1):
            _temp = _temp.next
            if _temp is None:
                break
        if _temp is None:
            return
        if _temp.next is None:
            return

        pointer = _temp.next.next
        _temp.next = None
        _temp.next = pointer

    # delete the linkedlist
    def deleteList(self):
        current  = self.head
        while current:
            prev = current.next
            del current
            current = prev

    def search(self, key):
        current= self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(2)
print("\nLinked List after Deletion at position 4: ")
llist.printList()
print("\nAfter Deletion of Linked List")
llist.deleteList()
print("\nBefore Deletion of Linked List")
llist.printList()

print("\n", llist.search(12))
