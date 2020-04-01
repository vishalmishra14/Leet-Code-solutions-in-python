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

    def pushList(self, new_data):
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data

    def inserAfter(self, prev_node, new_data):
        if prev_node is None:
            print('The given previous node must in LinkedList')
            return None

        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node


if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    node2 = Node(2)
    node3 = Node(4)

    llist.head.next = node2
    node2.next = node3

    llist.pushList(0)
    llist.inserAfter(node2, 3)
    llist.printList()