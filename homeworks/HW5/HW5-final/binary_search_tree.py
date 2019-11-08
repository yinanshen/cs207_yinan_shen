class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if node:
            if key < node.key:
                node.left = self._put(node.left, key, val)
                node.size = 1 + self._size(node.left) + self._size(node.right)
                return node
            elif key > node.key:
                node.right = self._put(node.right, key, val)
                node.size = 1 + self._size(node.left) + self._size(node.right)
                return node
            elif key == node.key:
                node.val = val
                return node
        else:
            node = BSTNode(key, val)
            return node

    def _get(self, node, key):
        if node == None:
            raise KeyError("no such node is found in the tree")
        if node.key == key:
            return node.val
        elif key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    @staticmethod
    def _size(node):
        return node.size if node else 0
