"""
Module solution for 35th mini task
Salimov Rustam
23.09.2023
"""

from union_find import UnionFind


def solution_no_union_find(data: list) -> (list, int):
    """Solution with no using of UnionFind

    Args:
        data (list): input data

    Returns:
        int: total fine
    """
    data.sort(key=lambda x: x[2], reverse=True)
    deadlines = []
    fines = []
    names = []
    total_fine = 0
    for name, deadline, fine in data:
        names.append(name)
        deadlines.append(deadline)
        fines.append(fine)

    time_table = [0] * len(deadlines)

    def insert(index, deadline):
        nonlocal total_fine
        if time_table[deadline] == 0:
            time_table[deadline] = names[index]
        else:
            while (deadline >= 0 and time_table[deadline] != 0):
                deadline -= 1
            if deadline < 0:
                insert(index, len(time_table) - 1)
                total_fine += fines[index]
            else:
                time_table[deadline] = names[index]

    for index, deadline in enumerate(deadlines):
        insert(index, deadline - 1)

    return (time_table, total_fine)


def solution(data: list) -> (list, int):
    """Solution with using of UnionFind

    Args:
        data (list): input data

    Returns:
        int: Total fine
    """
    data.sort(key=lambda x: x[2], reverse=True)
    deadlines = []
    fines = []
    names = []
    total_fine = 0
    for name, deadline, fine in data:
        names.append(name)
        deadlines.append(deadline)
        fines.append(fine)

    lefties = list(range(len(deadlines) + 1))
    time_table = UnionFind(list(range(len(deadlines) + 1)))
    time_table_names = [0] * len(deadlines)

    for index, deadline in enumerate(deadlines):
        name = names[index]
        fine = fines[index]

        index_class = time_table.find(deadline)
        place_to_put = lefties[index_class]

        if place_to_put <= 0:
            index_class = time_table.find(len(deadlines))
            place_to_put = lefties[index_class]
            total_fine += fine

        time_table_names[place_to_put - 1] = name
        new_leftie = min(place_to_put - 1, lefties[time_table.find(place_to_put - 1)])

        time_table.union(place_to_put, place_to_put - 1)

        lefties[time_table.find(place_to_put)] = new_leftie

    return (time_table_names, total_fine)


if __name__ == "__main__":
    print(solution([('A', 3, 25), ('B', 4, 10), ('C', 1, 30), ('D', 3, 50), ('E', 3, 20)]))
