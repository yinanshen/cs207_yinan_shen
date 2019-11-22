from math import floor
from typing import List
import math

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> str:
        return self.size

    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        min_idx = idx
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2

        if left_idx < self.size and self.compare(min_idx, left_idx):
            min_idx = left_idx

        if right_idx < self.size and self.compare(min_idx, right_idx):
            min_idx = right_idx

        if min_idx != idx:
            self.swap(idx,min_idx)
            self.heapify(min_idx)

    def build_heap(self) -> None:
        for i in range(self.size // 2, -1, -1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        self.size += 1
        self.elements += [key]
        self.build_heap()

    def heappop(self) -> int:
        if (len(self.elements) == 0):
            raise IndexError("Nothing to pop")
        smallest = self.elements[0]
        #self.elements = self.elements[1 : self.size]
        self.elements.remove(smallest)
        self.size -= 1
        self.build_heap()
        return smallest

class MinHeap(Heap):
    def compare(self, a: int, b: int):
        return self.elements[a] > self.elements[b]

class MaxHeap(Heap):
    def compare(self, a: int, b: int):
        return self.elements[a] < self.elements[b]
'''

#h = Heap([-1,0,0,15,23,1,2,3]) # The heap tree will be built during initialization
#print(h)

#elements = [1,2,3,4,5]
mn = MinHeap([1,2,3,4,5])
mx = MaxHeap([1,2,3,4,5])
print(mn)
print(mx)

mn.heappush(3.5)
print(mn)

print(mn.heappop())
print(mn)

h = MinHeap([-1,0,0,15,23,1,2,3])
print(h)

'''
