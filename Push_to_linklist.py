class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next

    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node


if __name__=='__main__':
    llist = LinkedList()

    llist.head = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    llist.head.next = node2
    node2.next = node3


    llist.push(0)

    llist.printList()

