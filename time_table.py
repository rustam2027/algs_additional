from union_find import UnionFind


def solution(data: list) -> int:
    data.sort(key=lambda x: x[1], reverse=True)

    deadlines = []
    fines = []

    for deadline, fine in data:
        deadlines.append(deadline)
        fines.append(fine)

    time_table = UnionFind([0] * len(data))

    print(deadlines)
    print(fines)
    print(time_table.value)


solution([(3, 25), (4, 10), (1, 30), (3, 50), (3, 20)])
