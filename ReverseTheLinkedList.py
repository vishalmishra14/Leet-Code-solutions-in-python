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

    def reversedLL(self):
        prev = None
        current = self.head
        _next = None

        while current:
            _next = current.next

            current.next = prev
            prev = current
            current = _next
        self.head = prev

    def printList(self):

        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    print("Given Linked List")
    llist.printList()
    llist.reversedLL()
    print("\nReversed Linked List")
    llist.printList()