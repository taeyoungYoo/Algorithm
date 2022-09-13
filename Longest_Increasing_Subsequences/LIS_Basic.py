'''
Longest increasing subsequences
주어진 배열 내에서 증가하는 부분 수열 중 가장 긴 수열을 말함
DP를 사용한 방법과 이분 탐색을 사용하는 방법으로 나뉜다.
'''

'''
DP apporach -> O(n^)
완전탐색보다는 효율적
i번째 인덱스에서 끝나는 최장 증가 수열의 길이를 구하며
0 ... i-1번째 인덱스 까지의 원소 중 i번째 원소보다 작은 원소에서 끝나는 LIS 중
가장 긴 subset을 선택해 거기에 자기 자신을 더하면 됨
'''

LIS_list = [1, 5, 4, 2, 3, 8, 6, 7, 9, 3, 4, 5]

def LIS_DP_LEN(lis : list) -> int:
    dp = [1] * len(lis)
    for i in range(len(lis)):
        for j in range(i):
            if lis[i] > lis[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

ret = LIS_DP_LEN(LIS_list)
print(ret)

'''
Binary search approach -> O(nlogn)
LIS 기록 배열을 하나 더 두고 처리
'''
from bisect import bisect_left

def LIS_Binary_LEN(lis : list) -> int:
    tmp = []
    tmp.append(lis[0])
    for i in range(1, len(lis)):
        if tmp[-1] < lis[i]:
            tmp.append(lis[i])
        else:
            replace_idx = bisect_left(tmp, lis[i])
            tmp[replace_idx] = lis[i]

    return len(tmp)
ret = LIS_Binary_LEN(LIS_list)
print(ret)

'''
Binary search approach -> O(nlogn)
앞선 경우에서는 LIS의 길이만을 구했다
실제 LIS 배열을 이분 탐색 방법을 적용해 구하자
'''
def LIS_Binary_Subset(lis : list) -> list:
    tmp = []
    index = []
    tmp.append(lis[0])
    index.append(0)
    for i in range(1, len(lis)):
        if tmp[-1] < lis[i]:
            index.append(len(tmp))
            tmp.append(lis[i])
        else:
            replace_idx = bisect_left(tmp, lis[i])
            tmp[replace_idx] = lis[i]
            index.append(replace_idx)
    ret = []
    next_idx = max(index)
    for i in range(len(lis)-1, -1, -1):
        if index[i] == next_idx:
            ret.append(lis[i])
            next_idx -= 1
    return ret[::-1]
ret = LIS_Binary_Subset(LIS_list)
print(ret)