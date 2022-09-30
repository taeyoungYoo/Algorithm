'''
    프로그래머스 여행 루트
    - 알파벳 순으로 탐색 루트 반환
    - 그래프 정렬 후 DFS 탐색
'''
from collections import defaultdict


route = ['ICN']
graph = defaultdict(list)


def find_route(node, target):
    if len(route) == target:
        return True
    if not graph[node]:
        return True
    for next_ in graph[node]:
        route.append(next_)
        keep = graph[node].pop(0)
        ret = find_route(next_, target)
        if not ret:
            graph[node].append(keep)
    route.pop()
    return False

def make_graph(tickets):
    lim = len(tickets)
    graph = defaultdict(list)
    for i in range(lim):
        graph[tickets[i][0]].append(tickets[i][1])
    for key in graph.keys():
        graph[key].sort()
    return graph


def solution(tickets):
    global route, graph
    graph = make_graph(tickets)
    print(graph)
    find_route('ICN', len(tickets) + 1)

    return route

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]
print(solution(tickets))
