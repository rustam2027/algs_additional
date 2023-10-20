"""
Module with class UnionFind
Salimov Rustam 
20.09.2023
"""


class UnionFind():
    """
    UnionFind class
    "объединение по рангам" и "сжатие путей"
    """
    def __init__(self, elements: list) -> None:
        self.value = elements
        self.rank = [0] * len(elements)

    def __str__(self) -> str:
        return str(self.value) + ' ' + str(self.rank)

    def find(self, element: int) -> int:
        """Return class of given element

        Returns:
            int: class of given element
        """
        current = element
        while current != self.value[current]:
            current = self.value[current]

        self.value[element] = current

        return current

    def union(self, element_one: int, element_two: int):
        """Unites class of element_one and element_two

        Args:
            element_one (int): first element
            element_two (int): second element
        """
        root_one = self.find(element_one)
        root_two = self.find(element_two)
        if root_one == root_two:
            return

        if self.rank[root_one] > self.rank[root_two]:
            self.value[root_one] = self.value[root_two]
        else:
            self.value[root_two] = self.value[root_one]
            if self.rank[root_one] == self.rank[root_two]:
                self.rank[root_two] += 1


def __union_tests():
    struct = UnionFind(list(range(10)))
    find_test_1 = []
    find_test_2 = []
    find_test_3 = []

    for i in range(10):
        find_test_1.append(struct.find(i))

    assert find_test_1 == list(range(10))

    for i in range(0, 10, 2):
        struct.union(i, i + 1)

    print(struct)
    struct.union(0, 2)
    print(struct)

    for i in range(10):
        find_test_2.append(struct.find(i))

    print(struct)
    struct.union(8, 6)
    struct.union(6, 4)
    print(struct)
    struct.union(3, 8)
    print(struct)
    for i in range(10):
        struct.find(i)
    print(struct)


# __union_tests()
