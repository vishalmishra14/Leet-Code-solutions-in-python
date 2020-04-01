class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):

        _temp = self.head

        if _temp is not None:
            if _temp.data == key:
                self.head = _temp.next
                _temp = None
                return

        while _temp is not None:
            if _temp.data == key:
                break
            prev = _temp
            _temp = _temp.next

        if _temp is None:
            return
        prev.next = _temp.next

        _temp = None

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

print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()