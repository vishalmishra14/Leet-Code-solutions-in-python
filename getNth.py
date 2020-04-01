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

    def Length(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return count

    def getNth(self, index):
        current = self.head
        count = 0
        while current:
            if count != index:
                count += 1
                current = current.next
            else:
                return current.data
        assert False, f"out of index: Length of the linkedlist {self.Length()} is less than passed value {index} "
        return 0

    def printList(self):

        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next


if __name__=='__main__':
    llist = LinkedList()

    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    n = 7

    print(f'Element at index 3 is: {llist.getNth(n)}')
