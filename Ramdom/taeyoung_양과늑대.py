'''
    프로그래머스 양과 늑대
    - DFS approach
    - 다음 방문 경로에 가지 않은 곳도 다 저장해서 다시 갈 수 있도록 함
'''
from collections import defaultdict


def find_max(node, sheep, wolf, visited, route, graph, info_gb):
    global answer
    print(node, ' ', sheep, ' ', wolf, ' ', route)
    visited[node] = 1
    if info_gb[node] == 0:
        sheep += 1
    else:
        wolf += 1
    if wolf >= sheep:
        return
    answer = max(answer, sheep)
    route += graph[node]
    for next_node in route:
        next_route = [nn for nn in route if nn != next_node and not visited[nn]]
        find_max(next_node, sheep, wolf, visited[:], next_route, graph, info_gb)


def solution(info, edges):
    global answer
    answer = 0
    info_gb = info
    visited = [0] * len(info)
    graph = defaultdict(list)
    for e in edges:
        graph[e[0]].append(e[1])
    find_max(0, 0, 0, visited, [], graph, info_gb)
    return answer
