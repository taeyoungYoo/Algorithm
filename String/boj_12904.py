'''
    BOJ 12904, A와 B
    - 문자열 수정 후 같아질 수 있는지 확인
    - 문자열 뒤 A 추가 혹은 뒤집고 뒤 B 추가
    - dfs 사용
'''

def solution():
    s = input()
    t = input()
    if s == t:
        print(1)
        return
    elif len(s) > len(t):
        print(0)
        return
    lim = len(s)
    while len(t) != lim:
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[:-1]
            t = t[::-1]
    if s == t:
        print(1)
    else:
        print(0)
    return

solution()


# DFS approach
# isPossible = False
# def dfs(init_str, result_str):
#     global isPossible
#     if len(init_str) == len(result_str) and init_str == result_str:
#         isPossible = True
#         return
#     elif len(init_str) == len(result_str):
#         return
#     dfs(init_str + 'A', result_str)
#     dfs(init_str[::-1] + 'B', result_str)
#
#
# def solution():
#     s = input()
#     t = input()
#     if len(s) > len(t):
#         print(0)
#         return
#     elif s == t:
#         print(1)
#         return
#     dfs(s, t)
#     if isPossible:
#         print(1)
#         return
#     else:
#         print(0)
#         return
#
# solution()