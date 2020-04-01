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

    # def append(self, new_data):
    #     new_node = Node(new_data)
    #     current = self.head
    #     while current:


    def printList(self):

        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


class Solution:
    def addTwoNumber(self, l1, l2):
        _addition = 0
        _div_10 = 0
        _remainder = 0
        _carry = 0
        p = l1.head
        q = l2.head
        l3 = LinkedList()
        while p:
            _addition = p.data + q.data + _carry
            _div_10 = _addition//10
            p = p.next
            q = q.next
            if _div_10 == 0:
                l3.push(_addition)
                continue
            _remainder = _addition % 10
            _carry = _div_10
            l3.push(_remainder)
        if _carry != 0:
            l3.push(_carry)
        self.reverseLL(l3)
        return l3

    def reverseLL(self, l: LinkedList) -> LinkedList:

        _prev = None
        _current = l.head
        _next = None

        while _current:
            _next = _current.next

            _current.next = _prev

            _prev = _current
            _current = _next
        l.head = _prev
        return l

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         result = Node(0)
#         result_tail = result
#         carry = 0
#
#         while l1 or l2 or carry:
#             val1 = (l1.data if l1 else 0)
#             val2 = (l2.data if l2 else 0)
#             carry, out = divmod(val1 + val2 + carry, 10)
#
#             result_tail.next = Node(out)
#             result_tail = result_tail.next
#
#             l1 = (l1.next if l1 else None)
#             l2 = (l2.next if l2 else None)
#
#         return result.next

if __name__ == '__main__':

    l1 = LinkedList()

    l1.push(8)
    l1.push(4)
    l1.push(9)

    l2 = LinkedList()

    l2.push(4)
    l2.push(6)
    l2.push(5)

    l1.printList()
    print("\n")
    l2.printList()
    sol = Solution()
    s1 = sol.addTwoNumber(l1, l2)
    print('\n')
    s1.printList()
