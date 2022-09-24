'''
    BOJ 16474 이상한 전깃줄
    - 오름차순 소팅 필요
    - 전봇대의 전깃줄은 1개만 있어야 함
'''
import collections
from itertools import combinations

def solution():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    rod = collections.defaultdict(list)
    k = int(input())
    for i in range(k):
        a, b = map(int, input().split())
        rod[a].append(b)
    rod = sorted(rod.items())
    graph = []
    print(rod)
    for i in range(int(2**(n-m))):
        tmp = []
        if len(rod[i][1]) != 1:
            tmp.append(rod[i][1].pop())
        else:
            tmp.append(rod[i][1][0])
        graph.append(tmp)
    for i in combinations([[0, 1], [2, 3]], 1):
        print(i)

solution()