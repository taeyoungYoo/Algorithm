'''
    BOJ 13711 LCS4
    LCS 크기 구하기
'''

n = int(input())
a = list(map(str, input().split()))
b = list(map(str, input().split()))
a = ''.join(a)
b = ''.join(b)

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(a)][len(b)])