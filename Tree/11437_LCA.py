# 최소 공통 조상 찾기
# 두 노드 사이의 거리: 루트부터 노드 A까지 거리 + 루트부터 노드 B까지 거리 - 2*LCA까지 거리
# O(NM)

import sys
sys.setrecursionlimit(int(1e5))

n = int(input())

parent = [0] * (n + 1)
d = [0] * (n + 1)
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, depth):
    visited[x] = True
    d[x] = depth
    for y in graph[x]:
        if visited[y]:
            continue
        parent[y] = x
        dfs(y, depth + 1)


def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


dfs(1, 0)

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))