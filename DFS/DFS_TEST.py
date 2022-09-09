# DFS test with python
# using recursive approach

count = 5


# basic form
def dfs_recursive(graph, start, cnt, visited=[]):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited


# Permutation
def dfs_permutation(graph, n):
    global candidate, visited
    if len(candidate) == n:
        print(candidate)
        return
    for i in range(len(graph)):
        if not visited[i]:
            candidate.append(graph[i])
            visited[i] = 1
            dfs_permutation(graph, n)
            candidate.pop()
            visited[i] = 0


# combination
def dfs_combination(idx, list):
    if len(list) == n:
        print(list)
        return
    for i in range(idx, len(graph)):
        dfs_combination(i+1, list+[graph[i]])

# combination
def dfs_combination_replacement(idx, list):
    if len(list) == n:
        print(list)
        return
    for i in range(idx, len(graph)):
        dfs_combination_replacement(idx+1, list+[graph[i]])


candidate = []
graph = [x for x in range(5)]
visited = [0 for _ in range(len(graph))]
n = 3

# dfs_permutation(graph, n)
dfs_combination(0, [])
