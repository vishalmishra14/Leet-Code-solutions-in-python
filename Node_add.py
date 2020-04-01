
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        _addition = 0
        _div_10 = 0
        _remainder = 0
        _carry = 0
        # p = l1.val
        # q = l2.val
        l3 = []
        len1 = self.checkLength(l1)
        len2 = self.checkLength(l2)

        if len1 > len2:
            l2 = self.append(l2, len1 - len2)
        else:
            l1 = self.append(l1, len2 - len1)

        while l1 or l2:
            _addition = l1.val + l2.val + _carry
            _div_10 = _addition//10
            l1 = l1.next
            l2 = l2.next
            if _div_10 == 0:
                _carry = _div_10
                l3.append(_addition)
                continue
            _remainder = _addition % 10
            _carry = _div_10
            l3.append(_remainder)
        if _carry != 0:
            l3.append(_carry)
        l4 = self.list2link(l3)
        # l5 = self.reverseLL(l4)
        return l4

    def append(self, lin, diff):
        new_list = []
        while lin:
            new_list.append(lin.val)
            lin = lin.next
        new_list.extend([0]*diff)
        new_Linklist = self.list2link(new_list)
        return new_Linklist



    def checkLength(self, nodelen):
        count = 0
        while nodelen:
            count += 1
            nodelen = nodelen.next
        return count


    def list2link(self, l):
        if len(l) == 0:
            return None
        ret_tail = ret_head = ListNode(l[0])
        for val in l[1:]:
            tmp = ListNode(val)
            ret_tail.next = tmp
            ret_tail = ret_tail.next
        return ret_head

    def printList(self,l):

        temp = l
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

    def reverseLL(self, l):
        _prev = None
        _current = l
        _next = None

        while _current:
            _next = _current.next

            _current.next = _prev

            _prev = _current
            _current = _next
        lh = _prev
        return lh


if __name__ == '__main__':
    solution = Solution()
    ll1 = solution.list2link([2, 7, 8, 9, 9, 9])
    solution.printList(ll1)
    print('\n')
    ll2 = solution.list2link([3, 7, 5])
    solution.printList(ll2)
    print('\n')
    ll3 = solution.addTwoNumbers(ll1, ll2)
    solution.printList(ll3)