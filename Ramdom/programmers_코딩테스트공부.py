'''
    프로그래머스 코딩테스트공부
    - DP approach
    - alp, cop에 대해 각각 DP 적용
'''


def solution(alp, cop, problems):
    INF = 987654321
    max_alp = 0
    max_cop = 0
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])
    min_alp = min(alp, max_alp)
    min_cop = min(cop, max_cop)
    dp = [[INF] * (max_cop+1) for _ in range(max_alp+1)]

    dp[min_alp][min_cop] = 0
    for i in range(min_alp, max_alp+1):
        for j in range(min_cop, max_cop+1):
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            for na, nc, ra, rc, cost in problems:
                if i >= na and j >= nc:
                    new_a = min(i+ra, max_alp)
                    new_c = min(j+rc, max_cop)
                    dp[new_a][new_c] = min(dp[new_a][new_c], dp[i][j]+cost)
    return dp[max_alp][max_cop]