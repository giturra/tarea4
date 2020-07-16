import numpy as np
from hashing.hash_estrategy1 import h
from hashing.base_hashing import BaseHash


def hp(x):
    m = np.power(2, 12)
    A = 0.61
    xA = np.multiply(x, A)
    return int(
        np.floor(np.multiply(m, xA - np.floor(xA)))
    )


class LinearHashG3(BaseHash):
    def __init__(self, size=10, hash_func=h, hash_func2=hp):
        super().__init__(size=size, hash_func=hash_func, hash_type='double')
        self.hp = hp

    def insert(self, element):
        pos = self.hash_func(element)
        pos2 = self.hash_func2(element)
        if not self.is_full():
            i = 1
            while not self.is_empty(pos):
                pos += i * pos2
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
