'''
    boj 1715 카드 섞기
    - Greedy 알고리즘
    - 우선순위 큐 적용
'''

import heapq

n = int(input())

ret = []
for i in range(n):
    heapq.heappush(ret, int(input()))

sum = 0
while len(ret) > 1:
    cand_1 = heapq.heappop(ret)
    cand_2 = heapq.heappop(ret)
    sum += cand_1 + cand_2
    heapq.heappush(ret, cand_1 + cand_2)
print(sum)