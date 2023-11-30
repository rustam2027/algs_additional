# https://leetcode.com/problems/create-sorted-array-through-instructions/submissions/
from typing import List, Dict


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        fenwick = FenwickTree(max(instructions) + 1)
        answer = 0
        calls: Dict[int, int] = {}
        for index, num in enumerate(instructions):
            less = fenwick.sum(num - 1)
            more = index - calls.get(num, 0) - less

            answer += min(less, more)

            # print(f"Insert {num} with cost min({less}, {more}) = {min(less, more)}, now nums = {fenwick.sums}")

            fenwick.update(num, 1)

            if num not in calls:
                calls[num] = 0
            calls[num] += 1

        return answer % (10 ** 9 + 7)


class FenwickTree:

    def __init__(self, n: int) -> None:
        self.sums: List[int] = [0] * n

    def sum(self, index: int) -> int:
        answer: int = 0
        while index >= 0:
            answer += self.sums[index]
            index = f(index) - 1
        return answer

    def update(self, index: int, num: int) -> None:
        while index < len(self.sums):
            self.sums[index] += num
            index = g(index)


def f(x: int) -> int:
    return x & (x + 1)


def g(x: int) -> int:
    return x | (x + 1)


def test():
    sol = Solution()
    ans = sol.createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2])
    assert ans == 4
