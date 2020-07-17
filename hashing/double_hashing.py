from base_hashing import BaseHash
import numpy as np

class DoubleHash(BaseHash):

    @staticmethod
    def random_prime(n, seed=None):
        """
        Returns random prime lower than n
        """
        if seed is not None:
            np.random.seed(seed)
        
        primes = [1] * (n + 1) 
        p = 2
        while p * p <= n : 
            if (primes[p] == 1): 
                for i in range(p * 2, n, p): 
                    primes[i] = 0
                    
            p += 1
        primes = np.array(primes[:-1]).nonzero()[0][2:]
        return np.random.choice(primes)

    def __init__(self, size=10, hash_func_1=None, hash_func_2=None, seed=None, update_size=False):
        super().__init__(size=size, hash_func=hash_func_1, hash_type='double')

        self.seed = seed
        self.update_size = update_size

        if hash_func_2 is None:
            # simple hash function
            # choose a prime lower than table size 
            # https://www.geeksforgeeks.org/double-hashing/
            # PRIME – (key % PRIME)
            
            self.prime = self.random_prime(len(self))
            self.hash_func_2 = lambda element : self.prime - (element % self.prime)

        else:
            self.hash_func_2 = hash_func_2

    def insert(self, element, return_comp=False):
        counter = 0
        idx = self.hash_func(element)
        i = 0

        collision_index = i * self.hash_func_2(element)
        insertion_index = idx + collision_index
        while True:
            calc_insert = self.is_empty(insertion_index) or self.deleted(insertion_index)
            counter += 1
            if calc_insert:
                self._hash_table[insertion_index] = element
                break
            else:  
                i += 1

                collision_index = i * self.hash_func_2(element)
                insertion_index = (idx + collision_index) % len(self)
                if insertion_index == idx:
                    # Table is full then double the size
                    # self._full()
                    if self.update_size:
                        self._full()
        if return_comp:
            return counter             
        return self
    
    def delete(self, element):
        idx = self.hash_func(element)
        i = 0
        
        collision_index = i * self.hash_func_2(element)
        insertion_index = idx + collision_index
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

                collision_index = i * self.hash_func_2(element)
                insertion_index = (idx + collision_index) % len(self)
                if insertion_index == idx:
                    # Table is full then double the size
                    # self._full()
                    return self

                continue
        
    def find(self, element):
        idx = self.hash_func(element)
        i = 0
        
        collision_index = i * self.hash_func_2(element)
        insertion_index = idx + collision_index
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
                
                collision_index = i * self.hash_func_2(element)
                insertion_index = (idx + collision_index) % len(self)
                if insertion_index == idx:
                    # Table is full then double the size
                    # self._full()
                    return self

                continue


if __name__ == "__main__":
    # Simple tests
    # Deberiamos formalizar

    
    hash = DoubleHash(10, seed=88)
    
    import numpy as np
    
    
    threes = np.ones(3, dtype=int) * 3
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
