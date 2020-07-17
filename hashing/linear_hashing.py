from base_hashing import BaseHash


class LinearHash(BaseHash):

    def __init__(self, size=10, hash_func=None, update_size=False):
        super().__init__(size=size, hash_func=hash_func, hash_type='linear')

        self.update_size = update_size

    def insert(self, element, return_comp=False):
        counter = 0
        idx = self.hash_func(element)
        i = 0
        insertion_index = idx + i
        while True:
            calc_insert = self.is_empty(insertion_index) or self.deleted(insertion_index)
            counter += 1 
            if calc_insert:
                self._hash_table[insertion_index] = element
                break
            else:
                i += 1
                insertion_index = (idx + i) % len(self)
                # print(insertion_index, idx)
                if insertion_index == idx:
                    # Table is full then double the size
                    print("Table is full")
                    if self.update_size:
                        self._full()
        if return_comp:
            return counter                
        return self

    def delete(self, element):
        idx = self.hash_func(element)
        i = 0
        insertion_index = idx + i
        while True:
            if self.is_empty(insertion_index):
                # Empty space, element is not in table
                return self
            elif self._hash_table[insertion_index] == element:
                # Delete the value
                self._hash_table[insertion_index] = self.empty_value
            else:
                # Keep looking
                i += 1
                insertion_index = (idx + i) % len(self)

                if insertion_index == idx:
                    # Table is full then double the size
                    print("Table is full")
                    # self._full()
                    return self

                continue

    def find(self, element):
        idx = self.hash_func(element)
        i = 0
        insertion_index = idx + i
        while True:
            if self.is_empty(insertion_index):
                # Empty space, element is not in table
                return False
            elif self._hash_table[insertion_index] == element:
                # Element found at insertion_index
                return True
            else:
                # Keep looking
                i += 1
                insertion_index = (idx + i) % len(self)

                if insertion_index == idx:
                    # Table is full then double the size
                    print("Table is full")
                    # self._full()
                    return self

                continue


if __name__ == "__main__":
    # Simple tests
    # Deberiamos formalizar
    hash = LinearHash(10)

    import numpy as np

    threes = np.ones(10, dtype=int) * 3
    ones = np.ones(3, dtype=int) * 1

    for i, one in enumerate(ones):
        hash.insert(one)
        print(f'{one} inserted')

    print(hash, '\n')

    hash.find(2)
    hash.delete(2)

    print('Tried to find and delete a 2\n')

    for i, three in enumerate(threes):
        hash.insert(three)
        print(f'{three} inserted')

    print(hash, '\n')

    hash.insert(2)
    print(2, 'inserted')
    print(hash, '\n')

    hash.find(2)
    hash.delete(2)
    print('Found and deleted a 2, result:', hash, '\n')
