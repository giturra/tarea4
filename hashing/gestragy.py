import random as rd
import numpy as np

"""
Al final seremos sólo los 2. Haré otra estrategias para cumplir a la otra persona.
"""


# http://profesores.elo.utfsm.cl/~agv/elo320/PLDS210/hash_func.html
# Ideas para funciones de hash

# ejemplo 1 h
def h(x):
    return x % np.power(2, 12)


# ejemplo 2 h prima
def hp(x):
    m = np.power(2, 12)
    A = 0.61
    xA = np.multiply(x, A)
    return int(
        np.floor(np.multiply(m, xA - np.floor(xA)))
    )


class HashTable(object):
    def __init__(self):
        # self.table = np.zeros(2 ** 25, dtype=int)
        self.table = [None] * (2 ** 25)

    def __len__(self):
        return len(self.table)

    def full(self):
        counter = 0
        for value in self.table:
            if value is not None:
                counter += 1
        if counter == self.__len__():
            return True
        return False

    def insert_a(self, x):
        pos = h(x)
        # print(pos)
        while self.table[pos] is not None and not self.full():
            pos += 1
        self.table[pos] = x

    def insert_b(self, x):
        # p random?
        p = rd.randint(1, 2 ** 12)
        pos = h(x)
        i = 1
        while self.table[pos] is not None and not self.full():
            pos += pos + i * p
        self.table[pos] = x

    def insert_c(self, x):
        pos = h(x)
        hprime = hp(x)
        i = 0
        while self.table[pos] is not None and not self.full():
            pos += pos + hprime * i
            i += 1
        self.table[pos] = x

    def delete(self, pos):
        self.table[pos] = None

    def search(self, value):
        for i in range(len(self.table)):
            if self.table[i] == value:
                return i
        return -1


if __name__ == '__main__':
    ht = HashTable()
    ht.insert_a(4096)
    print(ht.search(4096))
    ht.insert_a(4096*2)
    print(ht.search(4096*2))
    ht.insert_a(4096 * 3)
    print(ht.search(4096 * 3))
    print(ht.table[0])
    print(ht.table[1])
    print(ht.table[2])