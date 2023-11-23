
from typing import List


class Node:

    def __init__(self, value, left_index, right_index):
        self.value = value
        self.left_index = left_index
        self.right_index = right_index

    def __str__(self):
        return f"(value: {self.value}, l: {self.left_index}, r: {self.right_index})"

    def __repr__(self):
        return f"(value: {self.value}, l: {self.left_index}, r: {self.right_index})"


def binary_search(arr: List[int], value: int) -> int:
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] < value:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


class StrangeTree:

    def __init__(self, nums: list):
        self.arrays_int = [[]] * 5 * len(nums)
        self.arrays_node: List[List[Node]] = [[]] * 5 * len(nums)  # List[Node]

        def recursion_split_merge(nums: list, index: int) -> None:
            if len(nums) <= 1:
                self.arrays_int[index] = nums
                return
            delta = len(nums) >> 1

            new_nums_1 = nums[0:delta]
            new_nums_2 = nums[delta:len(nums)]

            recursion_split_merge(new_nums_1, index * 2 + 1)
            recursion_split_merge(new_nums_2, index * 2 + 2)

            self.arrays_int[index] = merge(self.arrays_int[index * 2 + 1], self.arrays_int[index * 2 + 2])

            node_array = []
            for num in self.arrays_int[index]:
                left = binary_search(self.arrays_int[index * 2 + 1], num)
                right = binary_search(self.arrays_int[index * 2 + 2], num)

                node_array.append(Node(num, left, right))

            self.arrays_node[index] = node_array

        def merge(nums_1: List[int], nums_2: List[int]) -> List[int]:
            merged_nums = []

            index_1 = 0
            index_2 = 0

            while index_1 < len(nums_1) and index_2 < len(nums_2):
                if nums_1[index_1] > nums_2[index_2]:
                    merged_nums.append(nums_1[index_1])
                    index_1 += 1
                else:
                    merged_nums.append(nums_2[index_2])
                    index_2 += 1

            while index_1 < len(nums_1):
                merged_nums.append(nums_1[index_1])
                index_1 += 1

            while index_2 < len(nums_2):
                merged_nums.append(nums_2[index_2])
                index_2 += 1

            return merged_nums

        recursion_split_merge(nums, 0)

    def __str__(self):
        return f"arrays_int: {str(self.arrays_int)} \narrays_node: {str(self.arrays_node)}"

    def less_or_equal(self, array_index: int, index: int, left_bound: int, right_bound: int, left: int,
                      right: int, value: int) -> int:
        if left_bound == left and right_bound == right:
            if self.arrays_int[array_index][index] == value:
                return len(self.arrays_node[array_index]) - index - 1
            else:
                return len(self.arrays_node[array_index]) - index

        delta = len(self.arrays_node[array_index]) >> 1
        observe_node = self.arrays_node[array_index][index]

        counter = 0
        if left < delta and observe_node.left_index != -1:
            counter += self.less_or_equal(array_index * 2 + 1, observe_node.left_index, left_bound, min(right, delta),
                                          left, min(right, delta), value)
        if right > delta + 1 and observe_node.right_index != -1:
            counter += self.less_or_equal(array_index * 2 + 2, observe_node.right_index, max(left_bound, delta + 1),
                                          right_bound, max(left_bound, delta + 1), right, value)
        return counter


class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        tree = StrangeTree(nums)

        return_list: List[int] = []
        for i, val in enumerate(nums):
            return_list.append(tree.less_or_equal(0, tree.arrays_int[0].index(val), 0, len(tree.arrays_node[0]), i,
                                                  len(tree.arrays_node[0]), val))

        return return_list


sol = Solution()
print(sol.countSmaller([-1, -1]))

# tree = StrangeTree([5, 2, 6, 1])
# print(tree)
