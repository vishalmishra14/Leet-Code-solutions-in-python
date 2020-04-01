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

    def insertafter(self,prev_node,new_data):

        if prev_node is None:
            print('the previous node is not in LinkedList')
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node


    def printList(self):
        while(self.head):
            print(self.head.data, end=" ")
            self.head = self.head.next


if __name__ == '__main__':
    llist = LinkedList()

    # llist.head = Node(1)
    # node2 = Node(2)
    # node3 = Node(4)
    #
    # llist.head.next = node2
    # node2.next = node3
    #
    # llist.push(0)
    # llist.insertafter(node2,3)
    # llist.append(5)
    # # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertafter(llist.head.next, 8)

    print('Created linked list is:',)
    llist.printList()

