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
        self.values = elements
        self.classes = list(range(len(elements)))
        self.rank = [0] * len(elements)

    def __str__(self) -> str:
        return str(self.values) + '\n' + str(self.classes) + '\n' + str(self.rank)

    def find(self, element: int) -> int:
        """Return class of given element

        Returns:
            int: class of given element
        """
        index = self.values.index(element)
        current = index
        while current != self.classes[current]:
            current = self.classes[current]

        self.classes[index] = current

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
            self.classes[root_two] = self.classes[root_one]
        else:
            self.classes[root_one] = self.classes[root_two]
            if self.rank[root_one] == self.rank[root_two]:
                self.rank[root_two] += 1


def __union_tests():
    struct_1 = UnionFind(list(range(10)))
    find_test_1 = []
    find_test_2 = []
    find_test_3 = []

    for i in range(10):
        find_test_1.append(struct_1.find(i))

    assert find_test_1 == list(range(10))

    for i in range(0, 10, 2):
        struct_1.union(i, i + 1)

    print(struct_1)
    struct_1.union(0, 2)
    print(struct_1)

    for i in range(10):
        find_test_2.append(struct_1.find(i))

    assert find_test_2 == [3, 3, 3, 3, 5, 5, 7, 7, 9, 9]

    for i in range(10):
        struct_1.union(0, i)

    for i in range(10):
        find_test_3.append(struct_1.find(i))

    assert find_test_3 == [3] * 10
    print(struct_1)

    struct_2 = UnionFind([50, 40, 20, 30])
    print(struct_2)
    struct_2.union(40, 20)
    print(struct_2)
    print(struct_2.find(40))
    print(struct_2.find(20))


if __name__ == "__main__":
    __union_tests()
