from typing import List
from StrangeTree import StrangeTree


class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        tree = StrangeTree(nums)
        print(tree)

        return_list: List[int] = []
        for i, val in enumerate(nums):
            return_list.append(tree.less_or_equal(i, len(tree.arrays_int[0]), val))
        return return_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSmaller([5, 2, 6, 1]))
