import numpy as np
from hashing.base_hashing import BaseHash


def h(x):
    return x % np.power(2, 12)


class LinearHashG1(BaseHash):
    def __init__(self, size=10, hash_func=h):
        super().__init__(size=size, hash_func=hash_func, hash_type='double')

    def insert(self, element):
        pos = self.hash_func(element)
        if not self.is_full():
            while not self.is_empty(pos):
                pos += 1
            self._hash_table[pos] = element
        else:
            return "Hash Full"

    def is_full(self):
        return self._size == len(self._hash_table)

    def search(self, element):
        pos = self.hash_func(element)
        while self._hash_table[pos] != element:
            pos += 1
        if pos == len(self._hash_table):
            return -1
        else:
            return pos

    def delete(self, element):
        pos = self.search(element)
        if pos != -1:
            self._hash_table[pos] = None
            return True
        return False


