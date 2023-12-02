class Node:

    def __init__(self, value, left_index, right_index):
        self.value = value
        self.left_index = left_index
        self.right_index = right_index

    def __str__(self):
        return f"(value: {self.value}, l: {self.left_index}, r: {self.right_index})"

    def __repr__(self):
        return f"(value: {self.value}, l: {self.left_index}, r: {self.right_index})"
