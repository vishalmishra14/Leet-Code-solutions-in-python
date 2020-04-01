class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

def inorder_no_re(root):
    s = []
    current = root
    while True:

        if current:
            s.append(current)
            current = current.left

        elif s:
            current = s.pop()
            print(current.key, end=" ")
            current = current.right

        else:
            break
    print()


def pre_order_no_re(root):

    stack = []
    current = root

    while True:

        if current and current not in stack:
            print(current.key, end=" ")
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            current = current.right
        else:
            break

    print()

def post_order_no_re(root):

    stack = []
    current = root
    done = []
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            if current.right is not None and current.right not in done:
                stack.append(current)
                current = current.right
            elif current not in done:
                done.append(current)
                print(current.key, end=' ')
                current = None
            else:
                break

        else:
            break
    print()

def inorder_with_no_stack(root):
    current = root
    while True:
        if current:
            if current.left is None and current:
                print(current.key, end=' ')
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right != current:
                    pre = pre.right
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    print(current.key, end=' ')
                    current = current.right
        else:
            break

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)

    # root = Node('A')
    # root.left = Node('B')
    # root.left.left = Node('D')
    # root.left.right = Node('E')
    # root.left.right.left = Node('F')
    # root.right = Node('C')
    # root.right.right = Node('G')
    # root.right.right.left = Node('H')

    inorder_no_re(root)
    pre_order_no_re(root)
    post_order_no_re(root)
    inorder_with_no_stack(root)