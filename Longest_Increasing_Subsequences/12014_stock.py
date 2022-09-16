'''
    백준 12014 주식
'''
from bisect import bisect_left


def lis(cand):
    tmp = []
    tmp.append(cand[0])
    for i in range(1, len(cand)):
        if tmp[-1] < cand[i]:
            tmp.append(cand[i])
        else:
            replace_idx = bisect_left(tmp, cand[i])
            tmp[replace_idx] = cand[i]
    return len(tmp)


def solution():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        stock_list = list(map(int, input().split()))
        ret = lis(stock_list)
        print(f"Case #{_ + 1}")
        if k <= ret:
            print(1)
        else:
            print(0)

solution()