from base_hashing import BaseHash

class LinearHash(BaseHash):
    
    def __init__(self, size=10):
        super().__init__(size=size)

    def insert(self, element):
        idx = super().hash_func(element)
        i = 0
        
        while True:
            insertion_index = (idx + i) % len(self)
            if self.is_empty(insertion_index) or self.deleted(insertion_index):
                self._hash_table[(idx + i) % len(self)] = element
                break
            else:  
                i += 1
                insertion_index = (idx + i) % len(self)
                if insertion_index == idx:
                    print(self, 'is full!')
                    return self
                    # self._full()
        return self
    
    def delete(self, element):
        idx = super().hash_func(element)
        i = 0

        while True:
            insertion_index = (idx + i) % len(self)
            
            if self.is_empty(insertion_index):
                print(element, "not in", self)
                return self
            elif self._hash_table[insertion_index] == element:
                self._hash_table[insertion_index] = self.empty_value
                print(element, 'deleted at index', insertion_index)
            else:
                i += 1
                continue
        
    def find(self, element):
        idx = super().hash_func(element)
        i = 0

        while True:
            insertion_index = (idx + i) % len(self)
            
            if self.is_empty(insertion_index):
                print(element, "not in", self)
                return False
            elif self._hash_table[insertion_index] == element:
                print(f'{element} is at index {insertion_index}', self)
                return True
            else:
                i += 1
                continue


if __name__ == "__main__":
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
