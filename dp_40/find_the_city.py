def findTheCity(n: int, edges, distanceThreshold: int) -> int:
    # Создаем матрицу
    cost = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

    # Заполняем тем что дано
    for u, v, distance in edges:
        cost[u][v] = distance
        cost[v][u] = distance

    # Приминяем алгоритм
    for via in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][via] + cost[via][j])

    # Заполняем доступные из каждого города
    reach = {}
    for i in range(n):
        c = 0
        for j in range(n):
            if cost[i][j] <= distanceThreshold and i != j:
                c += 1
        reach[i] = c

    m1 = min(reach.values())
    m2 = 0

    # Ищем минимальный и максимальный по номеру
    for city, reachable in reach.items():
        if m1 == reachable:
            m2 = max(m2, city)
    return m2


print(findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4))
