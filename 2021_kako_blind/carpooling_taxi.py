'''
카카오 2021 Blind Recruitment
합승 택시 요금

Floyd-warshall approach : O(V^3)
'''


# convert fares into 2-dim array, graph
def create_graph(n, fares):
    INF = 987654321
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0
    for x, y, z in fares:
        graph[x][y] = z
        graph[y][x] = z
    return graph


def solution(n, s, a, b, fares):
    answer = 987654321
    # graph initiation
    graph = create_graph(n, fares)
    # floyd-warshall
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    # find node i that minimize the cost to node a and b
    for i in range(1, n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer
