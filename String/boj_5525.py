'''
    BOJ 5525 IOIOI
    - 완전탐색 approach
    - KMP approach
'''


# 완전탐색 approach
def solution():
    n = int(input())
    m = int(input())
    S = input()
    P = 'IO' * n + 'I'
    lim = 2 * n + 1
    answer = 0
    for i in range(m-lim):
        if S[i] != 'I':
            continue
        else:
            isMatch = True
            for j in range(lim):
                if P[j] != S[i+j]:
                    isMatch = False
            if isMatch:
                answer += 1
    print(answer)


solution()