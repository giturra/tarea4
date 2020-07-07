import numpy as np

class BaseHash():

    def __init__(self, size):
        self._size = size
        self._hash_table = [None] * size

        self.empty_value = 'NaN'

    def insert(self, element):
        raise NotImplemented
    
    def delete(self, element):
        raise NotImplemented

    def search(self, element):
        raise NotImplemented
    
    def hash_func(self, element):
        return element % self._size

    def is_empty(self, idx, searching=False):
        if self._hash_table[idx] is None:
            return True
        else:
            return False
    
    def deleted(self, idx):
        if self._hash_table[idx] == self.empty_value:
            return True
        else:
            return False

    def _full(self):
        self.hash_table = self.hash_table + [None] * size
        self.size += size
    
    def __add__(self, idx, element):
        """
        Add element to hash table at given index.

        Will overwrite previous element at index. 
        """
        self._hash_table[idx] = element
    
    def __iter__(self):
        return iter(enumerate(self._hash_table))

    def __repr__(self):
        return repr(self._hash_table)
    
    def __len__(self):
        return len(self._hash_table)


