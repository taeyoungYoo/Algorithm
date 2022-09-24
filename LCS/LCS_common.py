'''
    Longest common subsequence
    일반적인 구현 코드
'''

# DP를 사용한 접근
# 최장 공통 부분 문자열의 길이를 구한다
a = 'abcieaodi'
b = 'bceakdi'

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(a)][len(b)])

# 실제 최장 공통 부분 문자열 구하기
