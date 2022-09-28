'''
    프로그래머스 여행 루트
    - 알파벳 순으로 탐색 루트 반환
    - 그래프 정렬 후 DFS 탐색
'''
from collections import defaultdict


route = ['ICN']
visited = []
graph = defaultdict(list)
answer = []


def find_route(node, target):
    global graph, route, answer
    if len(route) == target:
        answer = route.copy()
        return
    for next_ in graph[node]:
        try:
            check = visited.index([node, next_])
        except:
            return
        if visited[check] != 0:
            visited[check] = 0
            route.append(next_)
            find_route(next_, target)
            route.pop()
            visited[check] = [node, next_]


def make_graph(tickets):
    lim = len(tickets)
    graph = defaultdict(list)
    for i in range(lim):
        graph[tickets[i][0]].append(tickets[i][1])
    for key in graph.keys():
        graph[key].sort()
    return graph


def solution(tickets):
    global route, answer, visited, graph
    graph = make_graph(tickets)
    visited = tickets

    find_route('ICN', len(tickets) + 1)

    return answer

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]
print(solution(tickets))
