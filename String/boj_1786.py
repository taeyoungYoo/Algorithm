'''
    백준 1786, 찾기
    - KMP 알고리즘 적용
'''


def generate_pi(p):
    pi = [0] * len(p)
    pidx = 0
    for i in range(1, len(p)):
        while pidx > 0 and p[i] != p[pidx]:
            pidx = pi[pidx - 1]

        if (p[i] == p[pidx]):
            pidx += 1
            pi[i] = pidx
    return pi


def solution():
    T = input()
    P = input()
    pi = generate_pi(P)
    ret = []
    cnt = 0
    j = 0
    for i in range(0, len(T)):
        while j > 0 and T[i] != P[j]:
            j = pi[j - 1]
        if T[i] == P[j]:
            if j == (len(P) - 1):
                ret.append(i - len(P) + 2)
                cnt += 1
                j = pi[j]
            else:
                j += 1

    print(cnt)
    for l in ret:
        print(l)

solution()
