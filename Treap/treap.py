import random


class TreepNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(0, 99)
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None
        self._size = 0

    def _left_rotation(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        return y

    def _right_rotation(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        return x

    def _insert(self, root, key):
        if root is None:
            root = TreepNode(key)
            self._size += 1
            return root

        if key < root.key:
            root.left = self._insert(root.left, key)
            if root.left.priority > root.priority:
                root = self._right_rotation(root)
        elif key > root.key:
            root.right = self._insert(root.right, key)
            if root.right.priority > root.priority:
                root = self._left_rotation(root)
        else:
            raise Exception('No duplicates allowed')

        return root

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.left
            elif root.right is None:
                return root.right

            if root.left.priority > root.right.priority:
                root = self._right_rotation(root)
                root.right = self._delete(root.right, key)
            else:
                root = self._left_rotation(root)
                root.left = self._delete(root.left, key)
        self._size -= 1
        return root

    def _split(self, root, key):
        if root is None:
            return None, None

        if key < root.key:
            left, right = self._split(root.left, key)
            root.left = right
            return left, root
        else:
            left, right = self._split(root.right, key)
            root.right = left
            return root, right

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.priority > right.priority:
            left.right = self.merge(left.right, right)
            return left
        else:
            right.left = self.merge(left, right.left)
            return right

    def _search(self, root, key):

        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        elif key > root.key:
            return self._search(root.right, key)

    def _min(self, root):
        while root and root.left:
            root = root.left
        return root

    def _max(self, root):
        while root and root.right:
            root = root.right
        return root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def split(self, key):
        return self._split(self.root, key)

    def search(self, key):
        return self._search(self.root, key)

    def min(self):
        return self._min(self.root)

    def max(self):
        return self._max(self.root)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print("key:", root.key, "| priority:", root.priority, end="")
            if root.left:
                print(" | left child:", root.left.key, end="")
            if root.right:
                print(" | right child:", root.right.key, end="")
            print()
            self.inorder(root.right)

    def size(self):
        return self._size

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    mytreep = Treap()
    mytreep.insert(10)
    mytreep.insert(20)
    mytreep.insert(30)
    mytreep.insert(40)
    mytreep.insert(50)
    mytreep.insert(60)
    mytreep.inorder(mytreep.root)

    left, right = mytreep.split(40)

    print(f"Left : {left.key} and Right: {right.key}")

    data = mytreep.merge(left, right)

    print(f"Data : {data.key}")

    # print(f"{mytreep.search(10)}")
    # print(f"{mytreep.search(20)}")
    # print(f"{mytreep.search(30)}")
    # print(f"{mytreep.search(40)}")
    # print(f"{mytreep.search(50)}")
    # print(f"{mytreep.search(60)}")
    # print(f"{mytreep.search(100)}")
    #
    # print(f"{mytreep.max().key}")
    # print(f"{mytreep.min().key}")
