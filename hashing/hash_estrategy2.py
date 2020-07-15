from hashing.base_hashing import BaseHash
from hashing.hash_estrategy1 import h


class LinearHashG2(BaseHash):
    def __init__(self, size=10, hash_func=h, p=10):
        super().__init__(size=size, hash_func=hash_func, hash_type='double')
        self.p = p

    def insert(self, element):
        pos = self.hash_func(element)
        if not self.is_full():
            i = 1
            while not self.is_empty(pos):
                pos += i * self.p
            self._hash_table[pos] = element
        else:
            return "Hash Full"

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