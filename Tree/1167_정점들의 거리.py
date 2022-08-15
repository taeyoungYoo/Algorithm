import sys

sys.setrecursionlimit(10 ** 5)

Pmax = 20
n = int(input())
parent = [[0] * Pmax for _ in range(n + 1)]
length = [[0] * Pmax for _ in range(n + 1)]
visited = [False] * (n + 1)
d = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


# DFS or BFS for depth and length
def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for node in graph[x]:
        next_node = node[0]
        distance = node[1]
        if visited[next_node]:
            continue
        parent[next_node][0] = x
        length[next_node][0] = distance
        dfs(next_node, depth + 1)


# Recurrence relation
# Parent node of jth in ith == i-1th parent node of i-1th parent node
def set_parent():
    dfs(1, 0)
    for i in range(1, Pmax):
        for j in range(1, n + 1):
            # 각 노드에 대해 2**i번째 부모 정보 갱신
            if parent[j][i-1] != 0:
                parent[j][i] = parent[parent[j][i - 1]][i - 1]
                length[j][i] = length[j][i - 1] + length[parent[j][i - 1]][i - 1]


def lca(a, b):
    if d[a] > d[b]:
        a, b = b, a
    ret = 0
    for i in range(Pmax - 1, -1, -1):
        if d[b] - d[a] >= 2 ** i:
            ret += length[b][i]
            b = parent[b][i]

    if a == b:
        return ret

    for i in range(Pmax - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            ret += length[a][i] + length[b][i]
            a = parent[a][i]
            b = parent[b][i]

    ret += length[a][0] + length[b][0]
    return ret


set_parent()

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
