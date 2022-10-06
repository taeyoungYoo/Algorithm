'''
    프로그래머스 파괴되지 않은 건물
    - 완전탐색으로 접근할 경우 효율성 실패(O(N^3))
    - 이차원 누적합 적용
'''


def solution(board, skill):
    answer = 0

    acc_board = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for t, r1, c1, r2, c2, degree in skill:
        start = -1 if t == 1 else 1
        acc_board[r1][c1] += degree * start
        acc_board[r2+1][c2+1] += degree * start
        acc_board[r1][c2+1] += degree * start * -1
        acc_board[r2+1][c1] += degree * start * -1
    # 행 기준 누적합
    for i in range(len(acc_board)):
        for j in range(1, len(acc_board[0])):
            acc_board[i][j] += acc_board[i][j-1]
    # 열 기준 누적합
    for i in range(len(acc_board[0])):
        for j in range(1, len(acc_board)):
            acc_board[j][i] += acc_board[j-1][i]
    # board와 합산
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + acc_board[i][j] > 0:
                answer += 1
    return answer