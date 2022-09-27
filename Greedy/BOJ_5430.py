'''
    Boj 5430 AC
    - R 연산의 시간복잡도가 크니 flag를 사용
    - 최종 1번만 뒤집거나 뒤집지 않거나
    - D 연산은 deque의 popleft
    - 리스트 출력시 공백은 없어야하며 빈 리스트 출력시 []만 출력한다
'''
from collections import deque


def print_list(cand):
    lim = len(cand)
    if lim == 0:
        print('[]')
        return
    print('[', end='')
    for i in range(lim):
        if i != lim-1:
            print(cand[i], end=',')
        else:
            print(cand[i], end=']')
    print()


def get_result():
    isReverse = False
    operation = input()
    arr_len = int(input())
    arr_in = input()
    arr_in = arr_in[1:-1]
    arr_in = arr_in.split(',')
    arr = []
    for i in range(arr_len):
        arr.append(int(arr_in[i]))
    arr = deque(arr)
    lim = len(operation)
    check = ['R', 'D']
    for i in range(lim):
        if operation[i] not in check:
            print("error")
            return
        elif isReverse:
            if operation[i] == 'R':
                isReverse = False
            elif operation[i] == 'D' and not arr:
                print('error')
                return
            else:
                arr.pop()
        else:
            if operation[i] == 'R':
                isReverse = True
            elif operation[i] == 'D' and not arr:
                print('error')
                return
            else:
                arr.popleft()
    if isReverse:
        print_list(list(arr)[::-1])
    else:
        print_list(list(arr))


def solution():
    n = int(input())
    for i in range(n):
        get_result()


solution()