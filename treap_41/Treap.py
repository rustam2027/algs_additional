import random
import sys
from random import randrange


class TreapNode:

    def __init__(self, val, priority, left=None, right=None):

        self.val = val
        self.priority = priority
        self.left = left
        self.right = right
        self.size = 1
        self.sum = val


class Treap:
    def __init__(self, array=None, rand=True):

        self.random_priorities = random.sample(range(100), len(array))
        self.root = None

        if array and rand:
            self.root = self.random_pull(array)
        elif array and not rand:
            self.root = self.determined_pull(array)

    @staticmethod
    def update_size(treap: TreapNode):

        if treap is not None:
            treap.size = 1 + Treap.get_size(treap.left) + Treap.get_size(treap.right)

    @staticmethod
    def update_sum(treap: TreapNode):

        if treap is not None:
            treap.sum = treap.val + Treap.get_sum(treap.left) + Treap.get_sum(treap.right)

    @staticmethod
    def get_size(treap: TreapNode):

        if treap is not None:
            return treap.size
        return 0

    @staticmethod
    def get_sum(treap: TreapNode):

        if treap is not None:
            return treap.sum
        return 0

    def determined_pull(self, array):

        treap = None
        for index, item in enumerate(array):
            value, priority = item
            node = ImplicitTreapNode(value, priority)
            treap = self.insert(treap, node, index)
        return treap

    def random_pull(self, array=None):

        treap = None
        for index, elem in enumerate(array):
            rand_index = randrange(len(self.random_priorities))
            rand_priority = self.random_priorities[rand_index]
            self.random_priorities.remove(rand_priority)

            node = TreapNode(elem, rand_priority)
            treap = self.insert(treap, node, index)

        return treap

    def insert(self, treap: TreapNode, node: TreapNode, index: int):

        treap1, treap2 = self.split_by_size(treap, index)
        return self.merge(self.merge(treap1, node), treap2)

    @staticmethod
    def merge(treap1: TreapNode, treap2: TreapNode) -> TreapNode:

        if treap1 == None: return treap2
        if treap2 == None: return treap1

        if treap1.priority < treap2.priority:
            treap1.right = self.merge(treap1.right, treap2)
            self.update_size(treap1)
            self.update_sum(treap1)
            return treap1
        else:
            treap2.left = self.merge(treap1, treap2.left)
            self.update_size(treap2)
            self.update_sum(treap2)
            return treap2

    @staticmethod
    def split_by_size(treap: TreapNode, key: int) -> (TreapNode, TreapNode):

        if treap is None:
            return None, None

        left_size = get_size(treap.left)
        if key <= left_size:
            LL, LR = split_by_size(treap.left, key)
            treap.left = LR
            update_size(treap)
            update_sum(treap)
            return LL, treap
        else:
            RL, RR = split_by_size(treap.right, key - left_size - 1)
            treap.right = RL
            update_size(treap)
            update_sum(treap)
            return treap, RR

    def print_helper(self, node: TreapNode, indent: str, last: bool) -> None:

        if node:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(node.val, node.priority)
            self.print_helper(node.left, indent, False)
            self.print_helper(node.right, indent, True)

    def sum(self, start: int, end: int) -> int:
        L, R = self.split_by_size(self.root, start)
        RL, RR = self.split_by_size(R, end - start + 1)
        result = self.get_sum(RL)
        self.root = self.merge(self.merge(L, RL), RR)
        return result

