from base_hashing import BaseHash

class LinearHash(BaseHash):
    
    def __init__(self, size=10, hash_func=None):
        super().__init__(size=size, hash_func=hash_func)

    def insert(self, element):
        idx = super().hash_func(element)
        i = 0
        
        while True:
            insertion_index = super().hash_func(idx + i)
            if self.is_empty(insertion_index) or self.deleted(insertion_index):
                self._hash_table[insertion_index] = element
                break
            else:  
                i += 1
                insertion_index = super().hash_func(idx + i)
                if insertion_index == idx:
                    # Table is full then double the size
                    # self._full()
                    return self
        return self
    
    def delete(self, element):
        idx = super().hash_func(element)
        i = 0
        while True:
            insertion_index = super().hash_func(idx + i)
            if self.is_empty(insertion_index):
                # Empty space, element is not in table
                return self
            elif self._hash_table[insertion_index] == element:
                # Delete the value
                self._hash_table[insertion_index] = self.empty_value
            else:
                # Keep looking
                i += 1
                continue
        
    def find(self, element):
        idx = super().hash_func(element)
        i = 0
        while True:
            insertion_index = super().hash_func(idx + i)
            if self.is_empty(insertion_index):
                # Empty space, element is not in table
                return False
            elif self._hash_table[insertion_index] == element:
                # Element found at insertion_index
                return True
            else:
                # Keep looking
                i += 1
                continue


if __name__ == "__main__":
    # Simple tests
    # Deberiamos formalizar
    hash = LinearHash(10)
    
    import numpy as np
    
    threes = np.ones(3, dtype=int) * 3
    ones = np.ones(3, dtype=int) * 1
    
    for i, one in enumerate(ones):
        hash.insert(one)
        print(f'{one} inserted')

    print(hash, '\n')

    hash.find(2)
    hash.delete(2)

    print()

    for i, three in enumerate(threes):
        hash.insert(three)
        print(f'{three} inserted')
    
    print(hash, '\n')

    hash.insert(2)
    print(2, 'inserted')
    print(hash, '\n')
    
    hash.find(2)
    hash.delete(2)
