import numpy as np
import time

class BaseHash():

    def __init__(self, size, hash_func=None, hash_type=None):
        self._size = size
        self._original_size = size
        self._hash_table = [None] * size
        
        self._hash_type = hash_type

        if hash_func is None:
            # simple hash function
            self.hash_func = lambda element: element % self._size

        else:
            self.hash_func = hash_func

        self.empty_value = 'NaN'

        self._insert_times = None
        self._total_insert_times = None


    def insert(self, element):
        raise NotImplemented
    
    def delete(self, element):
        raise NotImplemented

    def search(self, element):
        raise NotImplemented

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
        self._hash_table = self._hash_table + [None] * self._size
        self._size += self._size
    
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

    def run_experiment(self, list_to_insert):
        counter = []
        insert_total = []
        insert_times = []
        start_total = time.time()
        
        for element in list_to_insert:
            start = time.time()
            counter.append(self.insert(element=element, return_comp = True))
            end = time.time()
            insert_times.append(end - start)
        end_total = time.time()    

        insert_total.append(end_total - start_total)
        self._insert_times = insert_times
        self._total_insert_times = insert_total
        self._comps = counter
        return self

    def get_results(self):
        return self._total_insert_times, self._insert_times, self._original_size, self._size, self._comps