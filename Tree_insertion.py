class newNode():
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def inorder(temp):

    if not temp:
        return
    inorder(temp.left)
    print(temp.key, end=' ')
    inorder(temp.right)


def insertion(temp, key):
    q = [temp]

    while len(q):
        _temp = q[0]
        q.pop(0)

        if not _temp.left:
            _temp.left = newNode(key)
            break
        else:
            q.append(_temp.left)

        if not _temp.right:
            _temp.right = newNode(key)
            break
        else:
            q.append(_temp.right)


if __name__ == '__main__':

    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)
    root.right.right = newNode(8)

    print('Inorder traversal before insertion:', end=' ')
    inorder(root)

    key = 12
    insertion(root, key)

    print()
    print("Inorder traversal after insertion:", end=' ')
    inorder(root)


