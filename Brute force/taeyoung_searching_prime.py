'''
    프로그래머스 소수 찾기
    - 모든 경우에 대해 소수인지 아닌지 판별
    - 에라토스테네스의 체로 최대 범위 소수 정리
    - 순열 활용 모든 경우의 수로 만들어 소수인지 확인
'''

from itertools import permutations

primes = []
# 에라토스테네스의 체
def eratosthenes(lim):
    global primes
    primes = [False, False] + [True] * (lim-1)
    for i in range(lim+1):
        if not primes[i]: continue
        for j in range(2 * i, lim + 1, i): primes[j] = False


def solution(numbers):
    answer = 0
    # 만들 수 있는 max value를 구해 그 이하의 소수 구하기
    worst = list(numbers)
    worst.sort(reverse=True)
    eratosthenes(int(''.join(worst)))
    numbers = list(numbers)
    # 만들 수 있는 경우의 수 소수인치 판별
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            if primes[int(''.join(j))]:
                primes[int(''.join(j))] = False
                answer += 1
    return answer