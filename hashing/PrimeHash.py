from hashing.base_hashing import BaseHash


class PrimeHash(BaseHash):
    def __init__(self, size=10, p=10, hash_func=None, update_size=False):
        super().__init__(size=size, hash_func=hash_func, hash_type='linear')
        self.p = p
        self.update_size = update_size

    def insert(self, element):
        idx = self.hash_func(element)
        i = 0

        insertion_index = idx + i
        while True:
            if self.is_empty(insertion_index) or self.deleted(insertion_index):
                self._hash_table[insertion_index] = element
                break
            else:
                i += 1
                insertion_index = (idx + (i * self.p)) % len(self)
                # print(insertion_index, idx)
                if insertion_index == idx:
                    # Table is full then double the size
                    # print("Table is full")
                    if self.update_size:
                        self._full()
                    return self
        return self

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
                insertion_index = (idx + (i * self.p)) % len(self)

                if insertion_index == idx:
                    # Table is full then double the size
                    print("Table is full")
                    # self._full()
                    return self

                continue

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
                insertion_index = (idx + (i * self.p)) % len(self)

                if insertion_index == idx:
                    # Table is full then double the size
                    print("Table is full")
                    # self._full()
                    return self

                continue
