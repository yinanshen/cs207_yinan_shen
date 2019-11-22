class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
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
        if not node:
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0


    def _removemin(self, node):
        if node == None:
            raise KeyError("There is nothing to remove..")
        if node.left == None:
            return node.right
        node.left = self._removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if node == None:
            raise KeyError("There is nothing to remove.")
        elif node.key == key:
            if node.left == None and node.right == None:
                return None
            elif node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                k = self.findminnode(node.right).key
                v = self.findminnode(node.right).val
                node.right = self._remove(node.right, k)
                node.key = k
                node.val = v
                return node

        elif node.key > key:
                node.left = self._remove(node.left, key)
        else:
            if node.right == None:
                raise KeyError("No such key is found in the BST")
                return node
            else:
                node.right = self._remove(node.right, key)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def findminnode(self, node):
        if node.left == None:
            return node
        else:
            return findminnode(node.left)

from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.tree = tree
        self.traversalType = traversalType
        self.results = []
        self.index = 0

    def __iter__(self):
        if self.traversalType == DFSTraversalTypes.PREORDER:
            return self.preorder(self.tree)
        elif self.traversalType == DFSTraversalTypes.INORDER:
            return self.inorder(self.tree)
        else:
            return self.postorder(self.tree)

    def __next__(self):
        try:
            results = self.results[self.index]
        except StopIteration:
            print("the entire BST has been traversed")
        self.index += 1
        return results

    def inorder(self, bst: BSTTable):
        self._inorder(bst._root)
        return iter(self.results)

    def _inorder(self, node):
        if node:
            #self._inorder(node.left)
            self._inorder(node.left)
            self.results.append(BSTNode(node.key, node.val))
            self._inorder(node.right)

    def preorder(self, bst: BSTTable):
        self._preorder(bst._root)
        return iter(self.results)

    def _preorder(self, node):
        if node:
            self.results.append(BSTNode(node.key, node.val))
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self, bst: BSTTable):
        self._postorder(bst._root)
        return iter(self.results)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            self.results.append(BSTNode(node.key, node.val))

'''
input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
bst = BSTTable()
for key, val in input_array:
    bst.put(key, val)
traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
for node in traversal:
    print(node.key, ', ', node.val)


t = BSTTable()
t.put(5, 'a')
t.put(15, 'a')
t.put(35, 'a')
t.put(45, 'a')
t.put(55, 'a')
t.put(54, 'a')
t.put(-5, 'b')
print(t._root)
print(t.remove(35))
print(t._root)



t = BSTTable()
t.put(5, 'a')
#t.put(1, 'b')
#t.put(2, 'c')
#t.put(0, 'd')
#print(t._root)
#print(t._removemin(t._root))
print(t.remove(10))




t = BSTTable()
t.put(5, 'a')
t.put(1, 'b')
t.put(2, 'c')
t.put(0, 'd')
#print(t._remove(t._root, 5))
#print(t._remove(t._remove(t._root, 5), 1))
print(t._remove(t._root, 10))
'''
