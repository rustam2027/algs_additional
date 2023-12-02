# https://leetcode.com/problems/count-of-smaller-numbers-after-self/submissions/
from typing import List


def find_first_smaller(arr, value):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < value:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


class SegmentTree:

    def __init__(self, nums: List[int]):
        self.len: int = len(nums)
        self.merge_tree: List[List[int]] = [[] for _ in range(4 * self.len + 1)]
        self._build_(nums, 0)

    def __str__(self):
        return f"len: {self.len}, merge_tree: {self.merge_tree}"

    def _build_(self, nums: List[int], index: int) -> None:
        if len(nums) <= 1:
            self.merge_tree[index] = nums
            return

        center: int = len(nums) >> 1

        self._build_(nums[0:center], index * 2 + 1)
        self._build_(nums[center:len(nums)], index * 2 + 2)

        self.merge_tree[index] = sorted(self.merge_tree[index * 2 + 1] + self.merge_tree[index * 2 + 2])

    def count_less(self, index: int, value: int) -> int:
        return self.count_less_recursion(value, 0, 0, self.len, index, self.len)

    def count_less_recursion(self, value: int, array_index: int, left_edge: int, right_edge: int, left: int,
                             right: int) -> int:
        if right_edge < left or left_edge > right:
            return 0

        if left_edge == left and right_edge == right:
            index_first_smaller = find_first_smaller(self.merge_tree[array_index], value)
            if index_first_smaller == -1:
                return 0
            return index_first_smaller + 1

        center: int = (right_edge + left_edge) >> 1

        counter: int = 0
        if left < center:
            counter += self.count_less_recursion(value, array_index * 2 + 1, left_edge, center, left,
                                                 min(right, center))
        if center < right:
            counter += self.count_less_recursion(value, array_index * 2 + 2, center, right_edge, max(left, center),
                                                 right)

        return counter


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        tree = SegmentTree(nums)

        answer: List[int] = []
        print(tree)

        for index, num in enumerate(nums):
            answer.append(tree.count_less(index, num))

        return answer


def test_2():
    array: List[int] = [5, 2, 6, 1]
    tree = SegmentTree(array)

    answer: List[int] = []
    print(tree)

    for index, num in enumerate(array):
        answer.append(tree.count_less(index, num))

    assert answer == [2, 1, 1, 0]


def test_3():
    array: List[int] = [0, 1, 2]
    tree = SegmentTree(array)

    answer: List[int] = []
    print(tree)

    for index, num in enumerate(array):
        answer.append(tree.count_less(index, num))

    assert answer == [0, 0, 0]


def test_5():
    array: List[int] = [6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]
    tree = SegmentTree(array)

    answer: List[int] = []
    print(tree)

    for index, num in enumerate(array):
        answer.append(tree.count_less(index, num))

    assert answer == [20, 20, 20, 20, 16, 16, 16, 16, 12, 12, 12, 12, 8, 8, 8, 8, 4, 4, 4, 4, 0, 0, 0, 0]
