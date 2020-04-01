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


    # hash way to detect loop:
    # def detectLoop(self):
    #
    #     s = set()
    #     temp = self.head
    #
    #     while temp:
    #         if temp in s:
    #             return True
    #
    #         s.add(temp)
    #         temp = temp.next
    #
    #     return False

    # Floyd's cycle finding Algorithm

    def detectLoop(self):
        s_p = f_p = self.head

        while s_p and f_p and f_p.next:
            s_p = s_p.next
            f_p = f_p.next.next
            if s_p == f_p:
                return True
        return False


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)

    llist.head.next.next.next.next = llist.head

    if llist.detectLoop():
        print('Loop Found')
    else:
        print('Loop Not Found')
