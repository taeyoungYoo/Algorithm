'''
    프로그래머스 최소직사각형
    - 완전탐색 풀이
    - index 0에 max값 몰아주고 max(index 0) * max(index(1)
'''

def solution(sizes):
    max_val = max(max(i) for i in sizes)
    min_val = max(min(i) for i in sizes)
    return max_val * min_val