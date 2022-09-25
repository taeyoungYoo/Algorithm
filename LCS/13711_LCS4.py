'''
    BOJ 13711 LCS4
    LCS 크기 구하기
    - 두 수열에는 중복되는 수가 없다
    - LIS 문제로 변경 후 O(nlogn) 적용
'''
import collections
from bisect import bisect_left

n = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
lis = []

dic_a = collections.defaultdict(int)

for i in range(n):
    dic_a[arr_1[i]] = i
for i in range(n):
    lis.append(dic_a[arr_2[i]])
tmp = []

tmp.append(lis[0])
for i in range(1, n):
    if tmp[-1] < lis[i]:
        tmp.append(lis[i])
    else:
        replace_idx = bisect_left(tmp, lis[i])
        tmp[replace_idx] = lis[i]
print(len(tmp))