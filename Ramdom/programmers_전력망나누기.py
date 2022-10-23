'''
    프로그래머스 전력망 둘로 나누기
    - link를 하나씩 제외해서 bfs로 탐색
'''
from collections import defaultdict,deque


def find_linked(node, n, graph):
    visited = [0] * n
    q = deque()
    q.append(node)
    ret = 1
    while q:
        cur_node = q.popleft()
        visited[cur_node] = 1
        for next in graph[cur_node]:
            if visited[next] == 1:
                continue
            q.append(next)
            ret += 1
    return ret


def solution(n, wires):
    answer = 100
    graph = defaultdict(list)
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    # brute force
    for wire in wires:
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        tmp = find_linked(wire[0], n+1, graph)
        answer = min(answer, abs(n-2*tmp))
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    return answer