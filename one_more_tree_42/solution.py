# https://leetcode.com/submissions/detail/1102085306/
import math
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0] * len(nums) * 4
        self.nums_size = len(nums)
        self.build(nums, 0, 0, len(nums) - 1)

    def build(self, a: List[int], v, tl, tr):
        if tl == tr:
            self.tree[v] = a[tl]
            return

        tm = (tl + tr) >> 1

        self.build(a, v * 2 + 1, tl, tm)
        self.build(a, v * 2 + 2, tm + 1, tr)

        self.tree[v] = self.tree[v * 2 + 1] + self.tree[v * 2 + 2]

    def update(self, index: int, val: int) -> None:
        def recursion_update(v: int, delta: int):
            self.tree[v] += delta

            ancestor = math.ceil(v / 2) - 1
            if ancestor >= 0:
                recursion_update(ancestor, delta)

        def recursion_find(v: int, tl: int, tr: int, index: int) -> int:
            if tl == tr == index:
                return v
            elif tl == tr and tl != index:
                print("Что-то не так")

            tm = (tl + tr) >> 1

            if index <= tm:
                return recursion_find(v * 2 + 1, tl, tm, index)
            else:
                return recursion_find(v * 2 + 2, tm + 1, tr, index)

        vertex = recursion_find(0, 0, self.nums_size - 1, index)

        delta = val - self.tree[vertex]

        recursion_update(vertex, delta)


        print(recursion_find(0, 0, self.nums_size - 1, index))

    def sumRange(self, left: int, right: int) -> int:
        def getSum(v, tl, tr, l, r: int) -> int:
            if l == tl and r == tr:
                return self.tree[v]

            tm = (tl + tr) >> 1
            res = 0
            if l <= tm:
                res += getSum(v * 2 + 1, tl, tm, l, min(r, tm))
            if r >= tm + 1:
                res += getSum(v * 2 + 2, tm + 1, tr, max(l, tm + 1), r)
            return res

        return getSum(0, 0, self.nums_size - 1, left, right)

    def __str__(self):
        return str(self.tree)


if __name__ == "__main__":
    a = NumArray([1, 2, 3])
    print(a)
    print(a.sumRange(2, 2))
    print(a.update(0, 2))
    print(a)
