"""
Module for testing solution of 35th mini task
Salimov Rustam
23.09.2023
"""

from time_table import solution
from time_table import solution_no_union_find


TESTS = [
    [[('A', 3, 25), ('B', 4, 10), ('C', 1, 30), ('D', 3, 50), ('E', 3, 20)], (['C', 'A', 'D', 'B', 'E'], 20)],
    [[('A', 3, 25), ('B', 4, 10), ('C', 1, 30), ('D', 3, 50), ('E', 3, 20), ('F', 3, 60), ('G', 5, 70), ('H', 1, 50)], (['H', 'D', 'F', 'B', 'G', 'E', 'A', 'C'], 75)],
    [[('A', 8, 25), ('B', 8, 10), ('C', 8, 30), ('D', 8, 50), ('E', 8, 20), ('F', 8, 60), ('G', 8, 70), ('H', 8, 50)], (['B', 'E', 'A', 'C', 'H', 'D', 'F', 'G'], 0)],
    [[('A', 1, 25), ('B', 1, 10), ('C', 1, 30), ('D', 1, 50), ('E', 1, 20), ('F', 1, 60), ('G', 1, 70), ('H', 1, 50)], (['G', 'B', 'E', 'A', 'C', 'H', 'D', 'F'], 245)]
]


def _make_tests_(index: int):
    print(solution_no_union_find(TESTS[index][0]))


if __name__ == '__main__':
    _make_tests_(3)


def make(index: int):
    assert solution(TESTS[index][0]) == TESTS[index][1]


def test_0():
    make(0)


def test_1():
    make(1)


def test_2():
    make(2)


def test_3():
    make(3)
