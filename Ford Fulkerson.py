# функція для знаходження шляху в графі з максимальною пропускною здатністю
def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return True if visited[t] else False


# функція для знаходження максимального потоку в графі
def ford_fulkerson(graph, source, sink):
    # копія графу для збереження оригінальних ваг ребер
    residual_graph = [graph[i].copy() for i in range(len(graph))]
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(residual_graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
    return max_flow


# зчитування матриці з файлу
with open("Lab4.txt") as f:
    # розмірність матриці
    n = int(f.readline().strip())
    # матриця
    graph = [[int(x) for x in f.readline().split()] for i in range(n)]

# виклик функції для знаходження максимального потоку
max_flow = ford_fulkerson(graph, 0, n - 1)

# виведення результату
print("Максимальний потік в графі: {}".format(max_flow))